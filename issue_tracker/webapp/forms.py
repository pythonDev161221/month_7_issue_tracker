from django import forms
from django.core.exceptions import ValidationError

from .models import Type, Status, Issue, Project


# class IssueForm(forms.Form):
#     summary = forms.CharField(max_length=200, required=True)
#     description = forms.CharField(max_length=2000, required=False, widget=forms.Textarea)
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True)
#     # type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True)
#     type_names = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),
#                                                 required=False, label='Типы',
#                                                 widget=forms.CheckboxSelectMultiple)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = []
        widgets = {
            'type_names': forms.CheckboxSelectMultiple
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['summary'] == cleaned_data['description']:
            raise ValidationError('Description should not duplicate title')
        return cleaned_data


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = []
