from decimal import Decimal as D

from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

from todovoodoo.core.models import ListItem, TodoList, Station, StationItem, ReportEntry


class ListItemForm(forms.ModelForm):
    description = forms.CharField(label="Description", max_length=100)
    always_show = forms.BooleanField(
        label="Always show in master list",
        required=False,
        initial=False,
        widget=forms.CheckboxInput,
    )

    def __init__(self, *args, **kwargs):
        super(ListItemForm, self).__init__(*args, **kwargs)
        self.fields["description"].widget.attrs.update({"autofocus": "autofocus"})

    class Meta:
        model = ListItem
        fields = ("description", "always_show")


class TodoListForm(forms.ModelForm):
    name = forms.CharField(label="List Name", max_length=100)
    interval = forms.IntegerField(min_value=1, max_value=600)
    # weekdays = forms.TypedMultipleChoiceField(coerce=int, choices=TodoList.WEEKDAYS)

    class Meta:
        model = TodoList
        fields = ("name", "interval", "frequency")


# ----


class StationForm(forms.ModelForm):
    name = forms.CharField(label="Station Name", max_length=100)
    description = forms.CharField(label="Station Description", max_length=255)
    refund_value = forms.DecimalField(
        label="Refund awarded for report.", min_value=D("0"), max_digits=4, decimal_places=2
    )

    class Meta:
        model = Station
        fields = ("name", "description", "refund_value")


class StationItemForm(forms.ModelForm):
    description = forms.CharField(label="Station Item Description", max_length=255)

    def __init__(self, *args, **kwargs):
        super(StationItemForm, self).__init__(*args, **kwargs)
        self.fields["description"].widget.attrs.update({"autofocus": "autofocus"})

    class Meta:
        model = StationItem
        fields = ("description",)


class ReportEntryForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget(attrs={"class": "form-control"})
    )
    description = forms.Textarea()

    class Meta:
        model = ReportEntry
        fields = ("phone_number", "description", "photo_upload")
