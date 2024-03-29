from django import forms

from .models import Patient,Disaese

class Patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name','age','gender','protine' ]

        labels = {
            'name' : 'Name*',
            'age' : 'Age',
            'gender' : 'Gender*',
            'protine' : 'Protine Structure',
        }

        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Title of image',
                'rows' : 1,
                'cols' : 100,
                'type' : 'text'
            }),

            'age' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'rows' : 1,
                'cols' : 100,
                'type' : 'number',
            }),

            'gender' : forms.Select(attrs={
                'class' : 'form-control',
                'rows' : 1,
                'cols' : 100,
                'type' : 'options',
            }),

            'protine' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Protine structure',
                'rows' : 3,
                'cols' : 100,
                'type' : 'text'
            }),
        }


class Disease_form(forms.ModelForm):
    class Meta:
        model = Disaese
        fields = ['name','root_protine','patient' ]

        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Type of disease',
                'rows' : 1,
                'cols' : 100,
                'type' : 'text'
            }),

            'root_protine' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Struecute of Protine',
                'rows' : 1,
                'cols' : 100,
                'type' : 'text'
            }),

            'patient' : forms.Select(attrs={
                'class' : 'form-control',
                'rows' : 1,
                'cols' : 100,
                'type' : 'options',
            }),

        }