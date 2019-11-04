from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, CharField, OneToOneField, TextField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from fernet_fields import EncryptedCharField
from model_utils.models import TimeStampedModel


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    pushover_user_key = EncryptedCharField(
        _("Pushover User Key"), null=True, default=None, blank=True, max_length=255
    )
    pushover_api_token = EncryptedCharField(
        _("Pushover API Token"), null=True, default=None, blank=True, max_length=255
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
