from django import forms
from django.forms import widgets

from customer.models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [
            "package",
            "author",
            "fname",
            "lname",
            "email",
            "adults_no",
            "child_no",
            "nights_no",
            "date_chosen",
            "resolved",
        ]
        widgets = {
            "fname": forms.TextInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "Firstname",
                }
            ),
            "lname": forms.TextInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "Lastname",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "example@example.com",
                }
            ),
            "adults_no": forms.NumberInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "2",
                }
            ),
            "child_no": forms.NumberInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "2",
                }
            ),
            "nights_no": forms.NumberInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "2",
                }
            ),
            "date_chosen": forms.DateInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                }
            ),
        }
