from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.timezone import now, localdate
from django.views.generic import ListView, CreateView

from bestlists.core.models import MasterList, ListItem, TodoList


class MasterListView(LoginRequiredMixin, ListView):

    template_name = "core/master_list.html"
    context_object_name = "master_list"

    def get_queryset(self):
        return ListItem.objects.filter(todo_list__master_list__owner=self.request.user)


master_list_view = MasterListView.as_view()


class ListItemCreateView(LoginRequiredMixin, CreateView):

    model = ListItem
    fields = ["description"]
    success_url = reverse_lazy("core:master-list")

    def form_valid(self, form):
        master_list, _ = MasterList.objects.get_or_create(owner=self.request.user)
        todo_list, _ = TodoList.objects.get_or_create(
            name="main", master_list=master_list
        )
        form.instance.todo_list = todo_list
        form.instance.due_date = localdate(now())
        return super().form_valid(form)


create_item_list = ListItemCreateView.as_view()
