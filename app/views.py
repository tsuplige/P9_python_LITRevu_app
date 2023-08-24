from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'app/home.html')


def ticket(request):
    return render(request, 'app/ticket.html')


def ticket_update(request):
    return render(request, 'app/ticket_update.html')


def critique(request):
    return render(request, 'app/critique.html')


def critique_update(request):
    return render(request, 'app/critique_update.html')


def subscription(request):
    return render(request, 'app/subscription.html')
