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
        "Few reports submitted in the last week. Is the service down?",
        "Don't forget to submit sample reports so we have test data to work with.",
        "Do you even test?",
        "Is anybody out there? Just submit random photos, it's not that hard!",
        "Testers don’t like to break things; they like to dispel the illusion that things work.",
        "Pretty good testing is easy to do (that’s partly why some people like to say 'testing is dead'-- they think testing isn't needed as a special focus because they note that anyone can find at least some bugs some of the time). Excellent testing is quite hard to do.",
        "A pinch of probability is worth a pound of perhaps.",
        "Testing is not responsible for the bugs inserted into software any more than the sun is responsible for creating dust in the air.",
        "The problem is not that testing is the bottleneck. The problem is that you don't know what's in the bottle. That’s a problem that testing addresses.",
        "Discovering the unexpected is more important than confirming the known.",
    ]
    today = localdate(now())
    last_week = today - relativedelta(weeks=1)
    for user in User.objects.filter(
        pushover_user_key__isnull=False, pushover_api_token__isnull=False
    ):
        if ReportEntry.objects.filter(station__owner=user, created__gte=last_week).count() <= 3:
            client = Client(user_key=user.pushover_user_key, api_token=user.pushover_api_token)
            client.send_message(random.choice(messages), title="Todovoodoo: WARNING!", priority=1)


@job
def generate_weekly_report():
    today = localdate(now())
    last_week_sun = today + relativedelta(weekday=SU(-1))
    last_week_mon = last_week_sun + relativedelta(weekday=MO(-1))
    for user in User.objects.filter(
        pushover_user_key__isnull=False, pushover_api_token__isnull=False
    ):
        totals = (
            ReportEntry.objects.filter(
                station__owner=user, created__gte=last_week_mon, created__lte=last_week_sun
            )
            .values("phone_number")
            .annotate(total_refund=Sum("station__refund_value"))
        )
        message = "\n".join(
            [
                f"{total.get('phone_number', 'anonymous')}: ${total.get('total_refund')}"
                for total in totals
            ]
        )
        if message:
            Client(
                user_key=user.pushover_user_key, api_token=user.pushover_api_token
            ).send_message(
                message,
                title=f"Todovoodoo: Weekly Refund Report ({last_week_mon.isoformat()} -- {last_week_sun.isoformat()})",
                priority=1,
            )
