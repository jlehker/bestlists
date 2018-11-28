from django import forms

from bestlists.core.models import ListItem, TodoList


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
    interval_duration = forms.IntegerField(label="Duration", min_value=1, max_value=365)
    date_unit = forms.ChoiceField(label="Units", choices=TodoList.DATE_UNIT)

    class Meta:
        model = TodoList
        fields = ("name", "interval_duration", "date_unit")
