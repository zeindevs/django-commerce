from django import forms

from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"class": "w-full py-3 px-5 rounded-md border"}
            )
        }
