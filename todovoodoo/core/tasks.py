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
    username = "hatorgippie"
    message = "test test test"
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return

    if not (user.pushover_user_key and user.pushover_api_token):
        return

    client = Client(user_key=user.pushover_user_key, api_token=user.pushover_api_token)

    client.send_message(message, title="Important message from todovoodoo!", priority=2)
