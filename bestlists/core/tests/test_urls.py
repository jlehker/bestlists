import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_delete_list():
    assert reverse("core:delete-todo-list", kwargs={"pk": 1}) == "/app/delete_todo_list/1/"
    assert resolve("/app/delete_todo_list/1/").view_name == "core:delete-todo-list"


def test_create_list():
    assert reverse("core:create-todo-list") == "/app/create_todo_list/"
    assert resolve("/app/create_todo_list/").view_name == "core:create-todo-list"


def test_lists():
    assert reverse("core:lists-view") == "/app/lists"
    assert resolve("/app/lists").view_name == "core:lists-view"


def test_default_redirect():
    assert reverse("core:master-list") == "/app/"
    assert resolve("/app/").view_name == "core:master-list"
