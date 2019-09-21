from django import forms
from django.forms import widgets

from webapp.models import status_choices


class GuestbookForm(forms.Form):
    post_author_name = forms.CharField(max_length=200, required=True, label='Описание')
    text = forms.CharField(max_length=3000, required=True, label='Текст',   widget=widgets.Textarea)
    date = forms.CharField(max_length=3000, required=True, label='Дата', widget=widgets.SelectDateWidget)
    creation_date = forms.CharField(max_length=3000, required=True, label='Дата', widget=widgets.SelectDateWidget)
    change_date = forms.CharField(max_length=3000, required=True, label='Дата', widget=widgets.SelectDateWidget)
    status = forms.ChoiceField(required=True, label='статус', choices=status_choices)
