from django.urls import path

from bestlists.core.views import (
    master_list_view,
    todo_list_view,
    list_item_delete_view,
    list_item_create_view,
    todo_list_create_view,
    todo_list_delete_view,
)

app_name = "core"
urlpatterns = [
    path("", view=master_list_view, name="master-list"),
    path("lists", view=todo_list_view, name="lists-view"),
    path("lists/<int:pk>/", view=todo_list_view, name="lists-view"),
    path("create_list_item/<int:pk>/", view=list_item_create_view, name="create-item"),
    path(
        "delete_list_item/<int:pk>/<int:list_pk>/", view=list_item_delete_view, name="delete-item"
    ),
    path("create_todo_list/<int:list_pk>/", view=todo_list_create_view, name="create-todo-list"),
    path("delete_todo_list/<int:pk>/", view=todo_list_delete_view, name="delete-todo-list"),
]
