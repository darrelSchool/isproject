from django import forms
from django.contrib.auth.forms import unicodedata
from django.contrib.auth.views import AuthenticationForm
from django.forms import widgets

from tour_operator import models


class UsernameField(forms.CharField):
    def to_python(self, value):
        value = super().to_python(value)
        if self.max_length is not None and len(value) > self.max_length:
            # Normalization can increase the string length (e.g.
            # "ﬀ" -> "ff", "½" -> "1⁄2") but cannot reduce it, so there is no
            # point in normalizing invalid data. Moreover, Unicode
            # normalization is very slow on Windows and can be a DoS attack
            # vector.
            return value
        return unicodedata.normalize("NFKC", value)

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            "autocapitalize": "none",
            "autocomplete": "username",
        }


class CreateOperator(forms.ModelForm):
    class Meta:
        model = models.Operator
        fields = ["name", "email", "description"]


class CreatePackage(forms.ModelForm):
    class Meta:
        model = models.Package
        fields = ["title", "description", "visibility", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "to-pack-create-field"}),
            "description": forms.TextInput(attrs={"class": "to-pack-create-field"}),
            "visibility": forms.CheckboxInput(attrs={"class": "to-pack-create-field"}),
        }


class ModifyPackage(forms.ModelForm):
    class Meta:
        model = models.Package
        fields = ["title", "description", "visibility", "image"]


class AuthForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-input"})
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-input"}
        ),
    )
