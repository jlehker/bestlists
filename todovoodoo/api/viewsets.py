from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoListSerializer, ListItemSerializer
from todovoodoo.core.models import ListItem


class ViewSetBase(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAuthenticated]
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
