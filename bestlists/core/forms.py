from django import forms

from bestlists.core.models import ListItem, TodoList


class ListItemForm(forms.ModelForm):
    description = forms.CharField(label="Description", max_length=100)

    def __init__(self, *args, **kwargs):
        super(ListItemForm, self).__init__(*args, **kwargs)
        self.fields["description"].widget.attrs.update({"autofocus": ""})

    class Meta:
        model = ListItem
        fields = ("description",)


class TodoListForm(forms.ModelForm):
    name = forms.CharField(label="List Name", max_length=100)

    class Meta:
        model = TodoList
        fields = ("name",)
