from factory import DjangoModelFactory, Faker

from bestlists.core.models import TodoList


class TodoListFactory(DjangoModelFactory):

    owner = Faker("user_name")
    name = Faker("name")

    class Meta:
        model = TodoList
        django_get_or_create = ["name"]
