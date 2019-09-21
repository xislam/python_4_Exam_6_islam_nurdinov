from django import forms
from django.forms import widgets

from webapp.models import status_choices


class GuestbookForm(forms.Form):
    post_author_name = forms.CharField(max_length=200, required=True, label='Имя Автора')
    text = forms.CharField(max_length=3000, required=True, label='Текст',   widget=widgets.Textarea)
    email = forms.CharField(max_length=254, required=True, label='Email', widget=widgets.EmailInput)

