from django import forms

from bestlists.core.models import ListItem


class TodoItemForm(forms.ModelForm):
    description = forms.CharField(label="Description", max_length=100)

    class Meta:
        model = ListItem
        fields = ("description",)
