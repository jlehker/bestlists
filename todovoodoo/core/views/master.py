from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.timezone import now, localdate
from django.views import View
from django.views.generic import ListView

from todovoodoo.core.models import Station, ListItem


class MasterListView(LoginRequiredMixin, ListView):
    """ Master view that includes all stations QR codes. """

    model = Station
    template_name = "core/master_list.html"
    context_object_name = "master_list"
    paginate_by = 10

    def get_queryset(self):
        return Station.objects.filter(Q(owner=self.request.user))


master_list_view = MasterListView.as_view()


class TagView(LoginRequiredMixin, ListView):
    """ Master view that includes all stations QR codes. """

    model = Station
    template_name = "core/station_tags.html"
    context_object_name = "stations"
    paginate_by = 10

    def get_queryset(self):
        return Station.objects.filter(Q(owner=self.request.user))


station_tag_view = TagView.as_view()


class ListItemPostpone(LoginRequiredMixin, View):
    """ Handle postponing items to another date. """

    def post(self, request, *args, **kwargs):
        redirect_url = request.POST.get("next", reverse("core:master-list"))
        try:
            list_item = ListItem.objects.get(pub_id=self.kwargs["pub_id"])
            if list_item.always_show:
                messages.add_message(
                    request, messages.WARNING, "Item marked to always show in master."
                )
            else:
                list_item.postpone(int(request.POST.get("days", 0)))
        except (ListItem.DoesNotExist, ValueError):
            messages.add_message(request, messages.ERROR, "Couldn't postpone item.")
        else:
            messages.add_message(
                request, messages.WARNING, f"Postponed until {list_item.due_date.isoformat()}."
            )

        return redirect(redirect_url)


postpone_item_view = ListItemPostpone.as_view()


class ListItemComplete(LoginRequiredMixin, View):
    """ Handle postponing items to another date. """

    def post(self, request, *args, **kwargs):
        redirect_url = request.POST.get("next", reverse("core:master-list"))
        try:
            list_item = ListItem.objects.get(pub_id=self.kwargs["pub_id"])
            list_item.mark_complete()
            if list_item.always_show:
                messages.add_message(
                    request,
                    messages.INFO,
                    'Marking an item as complete will clear "Always show in master" property.',
                )
        except (ListItem.DoesNotExist, ValueError):
            messages.add_message(request, messages.ERROR, "Couldn't mark item complete.")
        else:
            messages.add_message(
                request, messages.INFO, f"Completed until {list_item.due_date.isoformat()}."
            )

        return redirect(redirect_url)


complete_item_view = ListItemComplete.as_view()
