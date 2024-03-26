from django import forms 

class ImageForm(forms.Form):
    InputImage = forms.FileField( max_length=200, required=False)