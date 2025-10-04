from django import forms
from .models import UploadedCV

class CVUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedCV
        fields = ['file']
