import random

from dateutil.relativedelta import MO, SU, relativedelta
from django.db.models import Avg, Count, Min, Sum
from django.utils.timezone import localdate, now
from django_rq import job
from pushover import Client
from sorl.thumbnail import get_thumbnail

from todovoodoo.core.models import ReportEntry
from todovoodoo.users.models import User


@job("pushover")
def send_pushover_notification(entry: ReportEntry, photo_url: str):
    user = entry.station.owner
    if not (user.pushover_user_key and user.pushover_api_token):
        return

    client = Client(user_key=user.pushover_user_key, api_token=user.pushover_api_token)
    message = (
        "<b><u>Phone Number</u>:</b> "
        f'<a href="tel:{entry.phone_number}"><i>{entry.phone_number}</i></a>\n'
        "\n<b><u>Message</u>:</b>\n"
        f'<font color="#777"><i>{entry.description}</i></font>\n'
    )
    client.send_message(
        message,
        html=1,
        title=f"User Report: {entry.station.name}",
        url=photo_url,
        url_title="Click to view full quality image.",
        attachment=get_thumbnail(entry.photo_upload, "300", quality=85),
    )


@job
def send_message():
    messages = [
        "I'm testing sending scheduled messages. Please ignore, or don't I don't care.",
        "Hey don't forget to submit lots of tests so I can check on load!",
        "This is pretty cool right? I'm sending these with random priorities so you can see the differences.",
        "Seriously please help me test! I just found a bug where old notifications had broken links. ",
        "I think we can use this to publish reports and send them to you periodically",
        "We can have this tally up the refunds that are due to people at the end of the week.",
        "Automated reports could be nicer if I can match phone numbers to Airbnb data.",
    ]
    priorities = [-1, 0, 1]
    for user in User.objects.filter(
        pushover_user_key__isnull=False, pushover_api_token__isnull=False
    ):
        message = random.choice(messages)
        priority = random.choice(priorities)
        client = Client(user_key=user.pushover_user_key, api_token=user.pushover_api_token)
        client.send_message(message, title="Important message from todovoodoo!", priority=priority)


@job
def generate_weekly_report():
    today = localdate(now())
    last_week_sun = today + relativedelta(weekday=SU(-1))
    last_week_mon = last_week_sun + relativedelta(weekday=MO(-1))
    for user in User.objects.filter(
        pushover_user_key__isnull=False, pushover_api_token__isnull=False
    ).prefetch_related("station_set"):
        entries = (
            user.station_set.station.filter(created__gte=last_week_mon, created__lte=last_week_sun)
            .values("phone_number")
            .annotate(total_refund=Sum("station__refund_value"))
        )
        client = Client(user_key=user.pushover_user_key, api_token=user.pushover_api_token)
        message = "\n".join([f"{entry.phone_number}: ${entry.total_refund}" for entry in entries])
        client.send_message(
            message,
            title=f"Todovoodoo: Weekly Refund Report ({last_week_mon.isoformat()} -- {last_week_sun.isoformat()})",
            priority=1,
        )
