from django import forms

from bestlists.core.models import ListItem


class TodoItemForm(forms.ModelForm):
    description = forms.CharField(label="Description", max_length=100)

    def __init__(self, *args, **kwargs):
        super(TodoItemForm, self).__init__(*args, **kwargs)
        self.fields["description"].widget.attrs.update({"autofocus": ""})

    class Meta:
        model = ListItem
        fields = ("description",)
