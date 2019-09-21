from django.contrib import admin
from webapp.models import Guestbook


class GuestbookAdmin(admin.ModelAdmin):

    list_display = ['post_author_name', 'email', 'text', 'creation_date ', 'change_date', 'status']
    list_filter = ['post_author_name', 'email', 'text', 'creation_date', 'change_date', 'status']
    search_fields = ['post_author_name', 'email']
    fields = ['post_author_name', 'email', 'text', 'creation_date', 'change_date', 'status']


admin.site.register(Guestbook, GuestbookAdmin)
# Register your models here.
