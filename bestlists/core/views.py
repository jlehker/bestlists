from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now, localdate
from django.views.generic import ListView, DeleteView, CreateView, TemplateView

from bestlists.core.forms import ListItemForm, TodoListForm
from bestlists.core.models import ListItem, TodoList


class MasterListView(LoginRequiredMixin, ListView):
    model = ListItem
    template_name = "core/master_list.html"
    context_object_name = "master_list"
    paginate_by = 10

    def get_queryset(self):
        return ListItem.objects.filter(
            todo_list__owner=self.request.user, due_date__lte=localdate(now())
        )


master_list_view = MasterListView.as_view()


class TodoListView(LoginRequiredMixin, TemplateView):

    template_name = "core/todo_list.html"

    def get_context_data(self, pk=None, **kwargs):
        """Use this to add extra context."""
        todo_lookup_args = {"pk": pk} if pk is not None else {"name": "main"}
        try:
            todo_list = TodoList.objects.get(owner=self.request.user, **todo_lookup_args)
        except TodoList.DoesNotExist:
            return redirect(reverse("core:lists-view"))
        context = super(TodoListView, self).get_context_data(**kwargs)
        context["todo_lists"] = TodoList.objects.filter(owner=self.request.user)
        context["list_items"] = todo_list.listitem_set.order_by("-created")
        context["active_list_pk"] = todo_list.pk
        context["can_delete"] = True if todo_list.name != "main" else False
        context["list_item_form"] = ListItemForm()
        context["todo_list_form"] = TodoListForm()
        return context


todo_list_view = TodoListView.as_view()


class ListItemCreate(LoginRequiredMixin, CreateView):

    form_class = ListItemForm
    model = ListItem

    def form_valid(self, form):
        try:
            todo_list = TodoList.objects.get(owner=self.request.user, pk=self.kwargs["pk"])
        except TodoList.DoesNotExist:
            return redirect(reverse("core:lists-view"))
        form.instance.todo_list = todo_list
        form.instance.due_date = localdate(now())
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("core:lists-view", kwargs={"pk": self.kwargs["pk"]})


list_item_create_view = ListItemCreate.as_view()


class ListItemDelete(LoginRequiredMixin, DeleteView):

    success_url = reverse_lazy("core:lists-view")

    def get_queryset(self):
        return ListItem.objects.filter(todo_list__owner=self.request.user)

    def get_success_url(self):
        return reverse("core:lists-view", kwargs={"pk": self.kwargs["list_pk"]})


list_item_delete_view = ListItemDelete.as_view()


class TodoListCreate(LoginRequiredMixin, CreateView):

    form_class = TodoListForm
    model = TodoList
    success_url = reverse_lazy("core:lists-view")

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
        except IntegrityError:
            messages.add_message(
                request, messages.ERROR, "All of your Todo List names must be unique."
            )
        return redirect(reverse("core:lists-view", kwargs={"pk": self.kwargs["list_pk"]}))

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


todo_list_create_view = TodoListCreate.as_view()


class TodoListDelete(LoginRequiredMixin, DeleteView):

    success_url = reverse_lazy("core:lists-view")

    def get_queryset(self):
        return TodoList.objects.filter(owner=self.request.user).exclude(name__iexact="main")


todo_list_delete_view = TodoListDelete.as_view()
