import datetime
import json
from calendar import day_name

from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY, WEEKLY, MONTHLY, YEARLY, weekday
from django.contrib.postgres import fields
from django.db import models
from django.forms import model_to_dict
from django.utils.timezone import localdate, now
from model_utils import Choices

from model_utils.models import TimeStampedModel

from bestlists.users.models import User


class ListItem(TimeStampedModel):
    todo_list = models.ForeignKey("TodoList", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    due_date = models.DateField()

    def postpone(self, days: int = 0):
        self.due_date = localdate(now()) + relativedelta(days=days)
        self.save(update_fields=["due_date"])

    def mark_complete(self):
        self.due_date = self._next_due_date
        self.save(update_fields=["due_date"])

    @property
    def _next_due_date(self) -> datetime.date:
        """ Calculates the next time item will appear in master list. """
        due_date, *_ = rrule(
            freq=self.todo_list.frequency,
            interval=self.todo_list.interval,
            count=1,
            dtstart=self.due_date + relativedelta(days=1),
            byweekday=(*[weekday(i) for i in self.todo_list.weekdays],),
        )
        return due_date.date()


class TodoList(TimeStampedModel):
    FREQUENCY = Choices(
        (DAILY, "daily", "Daily"),
        (WEEKLY, "weekly", "Weekly"),
        (MONTHLY, "monthly", "Monthly"),
        (YEARLY, "yearly", "Yearly"),
    )
    INTERVAL = [(i, i) for i in range(600)]
    WEEKDAYS = Choices(*[(num, name.lower(), name) for num, name in enumerate(day_name)])

    frequency = models.PositiveSmallIntegerField(choices=FREQUENCY, default=FREQUENCY.weekly)
    interval = models.PositiveSmallIntegerField(choices=INTERVAL, default=1)
    weekdays = fields.ArrayField(
        models.PositiveSmallIntegerField(default=WEEKDAYS.monday), size=8, default=list
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        unique_together = ("owner", "name")

    def add_todo(self, description: str, due_date: datetime.date) -> ListItem:
        return ListItem.objects.create(todo_list=self, description=description, due_date=due_date)

    @property
    def as_json(self) -> str:
        return json.dumps(model_to_dict(self))
