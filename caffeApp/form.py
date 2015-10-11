from django import forms


class ImageUploadForm(forms.Form):
    imagefile = forms.FileField(
        label='Select an image to classify file',
        help_text='max. 10MB'
    )
