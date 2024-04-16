from django import forms

from .models import Khejas

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewKhejasForm(forms.ModelForm):
    class Meta:
        model = Khejas
        fields = ('category', 'name', 'description', 'rent', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'rent': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditKhejasForm(forms.ModelForm):
    class Meta:
        model = Khejas
        fields = ('name', 'description', 'rent', 'image', 'is_vacant')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'rent': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }