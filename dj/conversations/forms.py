from django import forms

from .models import ConversationsMessage

class ConversationsMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationsMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }