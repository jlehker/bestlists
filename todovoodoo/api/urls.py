from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .viewsets import TodoListViewSet, ListItemViewSet

app_name = "api"

schema_view = get_swagger_view(title="Todovoodoo API")

router = routers.DefaultRouter(trailing_slash=True)
router.register(r"lists", ListItemViewSet, basename="TodoList")
router.register(r"items", TodoListViewSet, basename="ListItem")

urlpatterns = [
    path("", schema_view),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
] + router.urls
