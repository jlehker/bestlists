from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from todovoodoo.core.models import TodoList


@receiver(user_signed_up)
def after_user_signed_up(request, user, *args, **kwargs):
    TodoList.objects.create(name="main", owner=user)
