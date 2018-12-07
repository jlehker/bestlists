from django.urls import path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .viewsets import TodoListViewSet, ListItemViewSet

app_name = "api"

schema_view = get_swagger_view(title="Todovoodoo API")

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"lists", ListItemViewSet, basename="TodoList")
router.register(r"items", TodoListViewSet, basename="ListItem")

urlpatterns = [path("", schema_view)] + router.urls
