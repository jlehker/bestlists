import random

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
