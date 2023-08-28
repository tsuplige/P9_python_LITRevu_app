from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from . import forms, models


@login_required
def home(request):
    tickets = list(models.Ticket.objects.all())
    reviews = list(models.Review.objects.all())

    combined_data = tickets + reviews

    sorted_data = sorted(combined_data, key=lambda x: x.time_created, reverse=True)

    return render(request, 'app/home.html', {'combined_data': sorted_data})


@login_required
def ticket_upload(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'app/ticket_upload.html', context={'form': form})
    # return render(request, 'app/ticket.html')


@login_required
def ticket_update(request, id):
    ticket = models.Ticket.objects.get(id=id)

    if request.method == 'POST':
        form = forms.TicketForm (request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.TicketForm(instance=ticket)

    return render(request, 'app/ticket_update.html', {'form': form})


@login_required
def ticket_delete(request, id):
    ticket = models.Ticket.objects.get(id=id)

    if request.method == 'POST':
        ticket.delete()
        return redirect('home')

    return render(request, 'app/ticket_delete.html', {'ticket': ticket})


@login_required
def ticket_answer(request):
    pass


@login_required
def review_upload(request):
    review_form = forms.ReviewForm()
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'app/review_upload.html', context=context)


@login_required
def review_update(request, id):
    review = models.Review.objects.get(id=id)

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.ReviewForm(instance=review)

    return render(request, 'app/review_update.html', {'form': form, 'ticket': review.ticket})


@login_required
def review_delete(request, id):
    review = models.Review.objects.get(id=id)

    if request.method == 'POST':
        review.delete()
        return redirect('home')

    return render(request, 'app/review_delete.html', {'review': review})


@login_required
def subscription(request):
    return render(request, 'app/subscription.html')
