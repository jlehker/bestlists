from django.urls import path

from bestlists.core.views import master_list_view, create_item_list

app_name = "core"
urlpatterns = [
    path("", view=master_list_view, name="master-list"),
    path("create_todo", view=create_item_list, name="create-item"),
]
