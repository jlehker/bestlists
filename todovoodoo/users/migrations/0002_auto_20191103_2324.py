# Generated by Django 2.2.6 on 2019-11-04 07:24

from django.db import migrations
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [("users", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="pushover_api_token",
            field=fernet_fields.fields.EncryptedCharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="Pushover API Token",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="pushover_user_key",
            field=fernet_fields.fields.EncryptedCharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="Pushover User Key",
            ),
        ),
    ]
