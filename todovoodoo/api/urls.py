from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view

from .viewsets import TodoListViewSet, ListItemViewSet

app_name = "api"

schema_view = get_swagger_view(title="Todovoodoo API")

router = routers.DefaultRouter(trailing_slash=True)
router.register(r"lists", ListItemViewSet, basename="TodoList")
router.register(r"items", TodoListViewSet, basename="ListItem")

urlpatterns = [
    path("", schema_view),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
