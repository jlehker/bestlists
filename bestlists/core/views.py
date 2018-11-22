from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.timezone import now, localdate
from django.views.generic import ListView, FormView

from bestlists.core.forms import TodoItemForm
from bestlists.core.models import ListItem, TodoList


class MasterListView(LoginRequiredMixin, ListView):

    template_name = "core/master_list.html"
    context_object_name = "master_list"

    def get_queryset(self):
        return ListItem.objects.filter(todo_list__owner=self.request.user)


master_list_view = MasterListView.as_view()


class TodoListView(LoginRequiredMixin, FormView):

    model = ListItem
    success_url = reverse_lazy("core:create-item")
    form_class = TodoItemForm
    template_name = "core/todo_list.html"

    def form_valid(self, form):
        todo_list, _ = TodoList.objects.get_or_create(name="main", owner=self.request.user)
        form.instance.todo_list = todo_list
        form.instance.due_date = localdate(now())
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        todo_list, _ = TodoList.objects.get_or_create(name="main", owner=self.request.user)
        context = super(TodoListView, self).get_context_data(**kwargs)
        context["list_items"] = todo_list.listitem_set.order_by("-created")
        context["list_name"] = f"{todo_list.name.capitalize()} List"
        return context


todo_list_view = TodoListView.as_view()
