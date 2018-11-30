import pytest
from datetime import date
from django.conf import settings

from todovoodoo.core.tests.factories import TodoListFactory

pytestmark = pytest.mark.django_db


def test_mark_complete(user: settings.AUTH_USER_MODEL):
    today = date.today()
    todo_list = TodoListFactory.create(owner=user)
    todo = todo_list.add_todo("test todo", today)
    todo.mark_complete()
    assert todo.due_date > today
