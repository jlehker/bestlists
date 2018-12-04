import uuid

import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_delete_list():
    pub_id = uuid.uuid4()
    assert (
        reverse("core:delete-todo-list", kwargs={"pub_id": str(pub_id)})
        == f"/v0/lists/delete/{pub_id}/"
    )
    assert resolve(f"/v0/lists/delete/{pub_id}/").view_name == "core:delete-todo-list"


def test_create_list():
    assert reverse("core:create-todo-list") == "/v0/lists/create/"
    assert resolve("/v0/lists/create/").view_name == "core:create-todo-list"


def test_lists():
    assert reverse("core:lists-view") == "/v0/lists"
    assert resolve("/v0/lists").view_name == "core:lists-view"


def test_default_redirect():
    assert reverse("core:master-list") == "/v0/"
    assert resolve("/v0/").view_name == "core:master-list"
