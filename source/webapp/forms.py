from django import forms
from django.forms import widgets




class GuestbookForm(forms.Form):
    post_author_name = forms.CharField(max_length=200, required=True, label='Имя Автора')
    text = forms.CharField(max_length=3000, required=True, label='Текст',   widget=widgets.Textarea)
    email = forms.CharField(max_length=254, required=True, label='Email', widget=widgets.EmailInput)


class SeacrhForm(forms.Form):
    author_name = forms.CharField(max_length=200, required=True, label='Имя')