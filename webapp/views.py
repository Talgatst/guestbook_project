from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import GuestBookReview
from webapp.forms import GuestBookForm


def index(request):
    reviews = GuestBookReview.objects.filter(status='active').order_by('-created_at')
    form = GuestBookForm()
    return render(request, 'index.html', {
        'reviews': reviews,
        'form': form,
    })


def add_review(request):
    if request.method == 'POST':
        form = GuestBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            reviews = GuestBookReview.objects.filter(status='active').order_by('-created_at')
            return render(request, 'index.html', {
                'reviews': reviews,
                'form': form,
                'notice': "Ошибка при добавлении",
            })
    return redirect('index')


def edit_review(request, pk):
    review = get_object_or_404(GuestBookReview, pk=pk)
    notice = None
    if request.method == 'POST':
        form = GuestBookForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            notice = "Ошибка при редактировании"
    else:
        form = GuestBookForm(instance=review)
    return render(request, 'edit_review.html', {'form': form, 'notice': notice})


def delete_review(request, pk):
    review = get_object_or_404(GuestBookReview, pk=pk)
    notice = None
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('index')
        email_input = request.POST.get('email')
        if email_input == review.email:
            review.delete()
            return redirect('index')
        else:
            notice = 'Неверный email'
    return render(request, 'delete_review.html', {'review': review, 'notice': notice})

