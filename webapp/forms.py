from django import forms
from webapp.models import GuestBookReview


class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBookReview
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст записи', 'rows': 3}),
        }
