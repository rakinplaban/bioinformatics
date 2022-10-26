from django import forms

from .models import Patient

class Patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['title','location', 'description','url' ]

        labels = {
            'title' : 'Title*',
            'location' : 'Location',
            'description' : 'Description*',
            'url' : '',
        }

        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Title of image',
                'rows' : 1,
                'cols' : 100,
                'type' : 'text'
            }),

            'url' : forms.ClearableFileInput(attrs={
                'class' : 'dropify',
                'rows' : 1,
                'cols' : 100,
                'type' : 'file',
                'multiple' : True,
                'data-height' : 100,
                # 'id' : 'upload_custom',
            }),

            'location' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'location',
                'rows' : 1,
                'cols' : 100,
                'type' : 'text',
            }),

            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Tell something about..',
                'rows' : 3,
                'cols' : 100,
                'type' : 'textarea'
            }),
        }

