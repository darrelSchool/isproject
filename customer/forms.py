from django import forms
from django.forms import widgets

from customer.models import Quote, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "email", "body", "rating"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "Your Name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "Your email",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "Write your review",
                    "rows": "3",
                }
            ),
            "rating": forms.NumberInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "0 - 5",
                    "min": "0",
                    "max": "5",
                }
            ),
        }


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [
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
                    "class": "px-3 py-2 border rounded-xl w-[200px]",
                    "placeholder": "2",
                    "min": "0",
                    "max": "20",
                }
            ),
            "child_no": forms.NumberInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl w-[200px]",
                    "placeholder": "2",
                    "min": "0",
                    "max": "20",
                }
            ),
            "nights_no": forms.NumberInput(
                attrs={
                    "class": "px-3 py-2 border rounded-xl w-[200px]",
                    "placeholder": "2",
                    "min": "0",
                    "max": "20",
                }
            ),
            "date_chosen": forms.DateInput(
                format=("%d/%m/%Y"),
                attrs={
                    "class": "px-3 py-2 border rounded-xl",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }
