from django.urls import path, include


from todovoodoo.core.views import (
    master_list_view,
    station_view,
    public_station_view,
    station_tag_view,
    list_item_delete_view,
    list_item_update_view,
    list_item_create_view,
    todo_list_create_view,
    todo_list_update_view,
    station_delete_view,
)

app_name = "core"
urlpatterns = [
    path("", view=master_list_view, name="master-list"),
    path("stations", view=station_view, name="lists-view"),
    path("stations/tags/", view=station_tag_view, name="tags-view"),
    path("stations/<uuid:pub_id>/", view=station_view, name="lists-view"),
    path("stations/create/", view=todo_list_create_view, name="create-todo-list"),
    path("stations/update/<uuid:pub_id>/", view=todo_list_update_view, name="update-todo-list"),
    path("stations/delete/<uuid:pub_id>/", view=station_delete_view, name="delete-station"),
    path("items/create/<uuid:pub_id>/", view=list_item_create_view, name="create-item"),
    path("items/update/<uuid:pub_id>/", view=list_item_update_view, name="update-item"),
    path("items/delete/<uuid:pub_id>/", view=list_item_delete_view, name="delete-item"),
    path("public/stations/", view=public_station_view, name="stations-public-view"),
    path("public/stations/<slug:slug>/", view=public_station_view, name="stations-public-view"),
]
