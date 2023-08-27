from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models


@login_required
def home(request):
    tickets = list(models.Ticket.objects.all())
    reviews = list(models.Review.objects.all())

    combined_data = tickets + reviews

    sorted_data = sorted(combined_data, key=lambda x: x.time_created, reverse=True)

    return render(request, 'app/home.html', {'combined_data': sorted_data})


def ticket_upload(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # set the uploader to the user before saving the model
            ticket.user = request.user
            # now we can save
            ticket.save()
            return redirect('home')
    return render(request, 'app/ticket_upload.html', context={'form': form})
    # return render(request, 'app/ticket.html')


def ticket_update(request):
    return render(request, 'app/ticket_update.html')


def critique(request):
    return render(request, 'app/critique.html')


def critique_update(request):
    return render(request, 'app/critique_update.html')


def subscription(request):
    return render(request, 'app/subscription.html')
