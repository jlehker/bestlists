from django.urls import path

from bestlists.core.views import (
    master_list_view,
    todo_list_view,
    list_item_delete_view,
    list_item_update_view,
    list_item_create_view,
    todo_list_create_view,
    todo_list_delete_view,
    postpone_item_view,
)

app_name = "core"
urlpatterns = [
    path("", view=master_list_view, name="master-list"),
    path("lists", view=todo_list_view, name="lists-view"),
    path("lists/<int:pk>/", view=todo_list_view, name="lists-view"),
    path("postpone_list_item/<int:pk>/", view=postpone_item_view, name="postpone-item"),
    path("create_list_item/<int:pk>/", view=list_item_create_view, name="create-item"),
    path("update_list_item/<int:pk>/", view=list_item_update_view, name="update-item"),
    path("delete_list_item/<int:pk>/", view=list_item_delete_view, name="delete-item"),
    path("create_todo_list/", view=todo_list_create_view, name="create-todo-list"),
    path("delete_todo_list/<int:pk>/", view=todo_list_delete_view, name="delete-todo-list"),
]
