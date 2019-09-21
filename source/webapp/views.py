from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import GuestbookForm
from webapp.models import Guestbook


def index_view(request, *args, **kwargs):
    guestbook = Guestbook.objects.all()
    return render(request, 'index.html', context={
        'guestbook': guestbook
    })


def guestbook_view(request, pk):
    guestbook = get_object_or_404Guestbook, pk=pk)
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
                date=form.cleaned_data['date'],
                text=form.cleaned_data['text'],
                status=form.cleaned_data['status']

            )

            return redirect('task_view', pk=guestbook.pk)

        else:

            return render(request, 'create.html', context={'form': form})


def guestbook_update_view(request, pk):
    guestbook = get_object_or_404(Guestbook, pk=pk)
    form = GuestbookForm(data=request.POST)

    if request.method == 'GET':
        form = GuestbookForm(data={
            'post_author_name': guestbook.post_author_name,
            'text': guestbook.text,
            'status': guestbook.status,
            'date': guestbook.date
        })
        return render(request, 'update.html', context={'guestbook': guestbook, 'form': form})

    elif request.method == 'POST':
        form = GuestbookForm(data=request.POST)
        if form.is_valid():
            guestbook.post_author_name = form.cleaned_data['post_author_name']
            guestbook.date = form.cleaned_data['date']
            guestbook.status = form.cleaned_data['status']
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


# def guestbook_seacrh(request):
#     if request.method == 'GET':
#          = request.GET.get('description')
#         guestbook = Guestbook.objects.filter(description__icontains=description)
#         return redirect('')
