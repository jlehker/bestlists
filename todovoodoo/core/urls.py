from django.urls import path

from todovoodoo.core.views import (
    master_list_view,
    todo_list_view,
    list_item_delete_view,
    list_item_update_view,
    list_item_create_view,
    todo_list_create_view,
    todo_list_update_view,
    todo_list_delete_view,
    postpone_item_view,
    complete_item_view,
)

app_name = "core"
urlpatterns = [
    path("", view=master_list_view, name="master-list"),
    path("lists", view=todo_list_view, name="lists-view"),
    path("lists/<uuid:pub_id>/", view=todo_list_view, name="lists-view"),
    path("lists/create/", view=todo_list_create_view, name="create-todo-list"),
    path("lists/update/<uuid:pub_id>/", view=todo_list_update_view, name="update-todo-list"),
    path("lists/delete/<uuid:pub_id>/", view=todo_list_delete_view, name="delete-todo-list"),
    path("items/postpone/<uuid:pub_id>/", view=postpone_item_view, name="postpone-item"),
    path("items/complete/<uuid:pub_id>/", view=complete_item_view, name="complete-item"),
    path("items/create/<uuid:pub_id>/", view=list_item_create_view, name="create-item"),
    path("items/update/<uuid:pub_id>/", view=list_item_update_view, name="update-item"),
    path("items/delete/<uuid:pub_id>/", view=list_item_delete_view, name="delete-item"),
]
