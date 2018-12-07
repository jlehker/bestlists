from rest_framework import routers

from .viewsets import TodoListViewSet, ListItemViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"lists", ListItemViewSet, basename="TodoList")
router.register(r"items", TodoListViewSet, basename="ListItem")

app_name = "api"
urlpatterns = router.urls
