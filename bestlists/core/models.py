import datetime

from django.db import models

from model_utils.models import TimeStampedModel

from bestlists.users.models import User


class ListItem(TimeStampedModel):
    todo_list = models.ForeignKey("TodoList", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    due_date = models.DateField()


class TodoList(TimeStampedModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(unique=True)

    def add_todo(self, description: str, due_date: datetime.date) -> ListItem:
        return ListItem.objects.create(todo_list=self, description=description, due_date=due_date)
