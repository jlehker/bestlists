from django.db import models

from model_utils.models import TimeStampedModel

from bestlists.users.models import User


class MasterList(TimeStampedModel):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)


class TodoList(TimeStampedModel):
    master_list = models.ForeignKey(MasterList, on_delete=models.CASCADE)
    name = models.TextField()


class ListItem(TimeStampedModel):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    due_date = models.DateField()
