import uuid

import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_delete_list():
    pub_id = uuid.uuid4()
    assert (
        reverse("core:delete-todo-list", kwargs={"pub_id": str(pub_id)})
        == f"/app/lists/delete/{pub_id}/"
    )
    assert resolve(f"/app/lists/delete/{pub_id}/").view_name == "core:delete-todo-list"


def test_create_list():
    assert reverse("core:create-todo-list") == "/app/lists/create/"
    assert resolve("/app/lists/create/").view_name == "core:create-todo-list"


def test_lists():
    assert reverse("core:lists-view") == "/app/lists"
    assert resolve("/app/lists").view_name == "core:lists-view"


def test_default_redirect():
    assert reverse("core:master-list") == "/app/"
    assert resolve("/app/").view_name == "core:master-list"
