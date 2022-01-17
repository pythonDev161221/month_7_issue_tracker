from django import forms
from .models import Type, Status


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True)
    description = forms.CharField(max_length=2000, required=False, widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True)
    # type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True)
    type_names = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),
                                                required=False, label='Типы',
                                                widget=forms.CheckboxSelectMultiple)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
