from django.urls import path

from bestlists.core.views import master_list_view, todo_list_view, delete_list_item_view

app_name = "core"
urlpatterns = [
    path("", view=master_list_view, name="master-list"),
    path("create_todo", view=todo_list_view, name="create-item"),
    path("delete_todo/<int:pk>/", view=delete_list_item_view, name="delete-item"),
]
