from django import forms
from .models import Lead
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name','email','phone','insurance_type','message']
        widgets = {'message': forms.Textarea(attrs={'rows':3}), 'name': forms.TextInput(), 'email': forms.EmailInput(), 'phone': forms.TextInput(), 'insurance_type': forms.Select(),}
