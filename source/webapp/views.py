from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import *
from webapp.models import Guestbook


def index_view(request, *args, **kwargs):
    guestbooks = Guestbook.objects.filter(status='active').order_by('-creation_date')
    form = SeacrhForm()
    return render(request, 'index.html', context={
        'guestbooks': guestbooks,
        'form': form
    })


def guestbook_view(request, pk):
    guestbook = get_object_or_404(Guestbook, pk=pk)
    return render(request, 'guestbook.html', context={'guestbook': guestbook})


def guestbook_create_view(request, *args, **kwargs):
    if request.method == 'GET':

        form = GuestbookForm()

        return render(request, 'create.html', context={'form': form})

    elif request.method == 'POST':
        form = GuestbookForm(data=request.POST)
        if form.is_valid():
            guestbook = Guestbook.objects.create(
                post_author_name=form.cleaned_data['post_author_name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],

            )

            return redirect('guestbook_view', pk=guestbook.pk)

        else:

            return render(request, 'create.html', context={'form': form})


def guestbook_update_view(request, pk):
    guestbook = get_object_or_404(Guestbook, pk=pk)
    form = GuestbookForm(data=request.POST)

    if request.method == 'GET':
        form = GuestbookForm(data={
            'post_author_name': guestbook.post_author_name,
            'text': guestbook.text,
            'email': guestbook.email,
        })
        return render(request, 'update.html', context={'guestbook': guestbook, 'form': form})

    elif request.method == 'POST':
        form = GuestbookForm(data=request.POST)
        if form.is_valid():
            guestbook.post_author_name = form.cleaned_data['post_author_name']
            guestbook.text = form.cleaned_data['text']
            guestbook.save()
            return redirect('guestbook_view', pk=guestbook.pk)


def guestbook_delete_view(request, pk):
    guestbook = get_object_or_404(Guestbook, pk=pk)

    if request.method == 'GET':
        return render(request, 'delete.html', context={'guestbook': guestbook})
    elif request.method == 'POST':
        guestbook.delete()
        return redirect('index')


def guestbook_seacrh(request):
    author_name = request.GET.get('search')
    guestbooks = Guestbook.objects.filter(post_author_name__contains=author_name).filter(status='active')
    return render(request, 'index.html', context={
        'guestbooks': guestbooks
    })


