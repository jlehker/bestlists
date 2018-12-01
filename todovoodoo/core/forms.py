from django import forms

from todovoodoo.core.models import ListItem, TodoList


class ListItemForm(forms.ModelForm):
    description = forms.CharField(label="Description", max_length=100)

    def __init__(self, *args, **kwargs):
        super(ListItemForm, self).__init__(*args, **kwargs)
        self.fields["description"].widget.attrs.update({"autofocus": "autofocus"})

    class Meta:
        model = ListItem
        fields = ("description",)


class TodoListForm(forms.ModelForm):
    name = forms.CharField(label="List Name", max_length=100)
    interval = forms.IntegerField(min_value=1, max_value=600)
    # weekdays = forms.TypedMultipleChoiceField(coerce=int, choices=TodoList.WEEKDAYS)

    class Meta:
        model = TodoList
        fields = ("name", "interval", "frequency")
