# Generated by Django 2.2.5 on 2019-09-04 05:48

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0004_reportentry_station")]

    operations = [
        migrations.AddField(
            model_name="station",
            name="refund_value",
            field=models.DecimalField(decimal_places=2, default=Decimal("0"), max_digits=9),
        )
    ]
