import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from model_utils import Choices

from model_utils.models import TimeStampedModel

from bestlists.users.models import User


class ListItem(TimeStampedModel):
    todo_list = models.ForeignKey("TodoList", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    due_date = models.DateField()

    def mark_complete(self):
        self.due_date += relativedelta(
            **{self.todo_list.date_unit: self.todo_list.interval_duration}
        )
        self.save(update_fields=["due_date"])


class TodoList(TimeStampedModel):
    DATE_UNIT = Choices("days", "weeks", "months", "years")

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    date_unit = models.CharField(choices=DATE_UNIT, default=DATE_UNIT.weeks, max_length=8)
    interval_duration = models.IntegerField(default=1)

    class Meta:
        unique_together = ("owner", "name")

    def add_todo(self, description: str, due_date: datetime.date) -> ListItem:
        return ListItem.objects.create(todo_list=self, description=description, due_date=due_date)
