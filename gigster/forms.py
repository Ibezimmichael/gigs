from django import forms
from .models import Gig, Company, Role

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['title']

class GigForm(forms.ModelForm):
    class Meta:
        model = Gig
        fields = ['title', 'description', 'company', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['role'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a title for your gig'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a description for your gig'})
