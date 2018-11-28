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
    complete_item_view,
)

app_name = "core"
urlpatterns = [
    path("", view=master_list_view, name="master-list"),
    path("lists", view=todo_list_view, name="lists-view"),
    path("lists/<int:pk>/", view=todo_list_view, name="lists-view"),
    path("lists/create/", view=todo_list_create_view, name="create-todo-list"),
    path("lists/delete/<int:pk>/", view=todo_list_delete_view, name="delete-todo-list"),
    path("items/postpone/<int:pk>/", view=postpone_item_view, name="postpone-item"),
    path("items/complete/<int:pk>/", view=complete_item_view, name="complete-item"),
    path("items/create/<int:pk>/", view=list_item_create_view, name="create-item"),
    path("items/update/<int:pk>/", view=list_item_update_view, name="update-item"),
    path("items/delete/<int:pk>/", view=list_item_delete_view, name="delete-item"),
]
