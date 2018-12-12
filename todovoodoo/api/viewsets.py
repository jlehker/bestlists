from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from todovoodoo.core.models import ListItem

from .serializers import TodoListSerializer, ListItemSerializer


class ViewSetBase(viewsets.ModelViewSet):
    """ Base viewset for user APIs """

    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend)
    lookup_field = "pub_id"


class TodoListViewSet(ViewSetBase):
    """ Viewset for retrieving and modifying lists. """

    serializer_class = TodoListSerializer

    def get_queryset(self):
        return self.request.user.todolist_set.all()


class ListItemViewSet(ViewSetBase):
    """ Viewset for retrieving and modifying list items. """

    serializer_class = ListItemSerializer

    def get_queryset(self):
        return ListItem.objects.filter(todo_list__owner=self.request.user)
