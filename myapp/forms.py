from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo':'Upload Photo','name':'','file':'Upload File'}

        widgets = {
            'photo':forms.ClearableFileInput(attrs={'class':'form-control',}),
            
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name Here'}),

            'file':forms.ClearableFileInput(attrs={'class':'form-control',}),
        }
