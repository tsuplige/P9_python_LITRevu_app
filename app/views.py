from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from authentication.models import User
from . import forms, models
from django.conf import settings


@login_required
def home(request):
    data = get_user_and_followed_article(request.user, False)

    return render(request, 'app/home.html', {'combined_data': data})


@login_required
def user_self_posts(request):
    data = get_user_and_followed_article(request.user, True)

    return render(request, 'app/home.html', {'combined_data': data})


@login_required
def users_self_posts(request, id):
    user = User.objects.get(id=id)
    data = get_user_and_followed_article(user, True)
    user_page = {
        'is_user_page': True,
        'user': user,
        }
    return render(request, 'app/home.html', {'combined_data': data,
                                             'user_page': user_page})


def get_user_and_followed_article(user, only_user):
    reviews = list(models.Review.objects.filter(user=user))
    tickets = list(models.Ticket.objects.filter(user=user))
    if only_user is not True:
        followed_users = user.following.all()
        for data in followed_users:
            reviews += list(models.Review.objects.filter(user=data.followed_user))
            tickets += list(models.Ticket.objects.filter(user=data.followed_user))

    combined_data = tickets + reviews

    sorted_data = sorted(combined_data, key=lambda x: x.time_created,
                         reverse=True)

    return sorted_data


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
        if request.user == review.user or request.user.is_superuser:
            form = forms.TicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('home')
        return redirect('home')
    else:
        form = forms.TicketForm(instance=ticket)

    return render(request, 'app/ticket_update.html', {'form': form})


@login_required
def ticket_delete(request, id):
    ticket = models.Ticket.objects.get(id=id)

    if request.method == 'POST':
        if request.user == ticket.user or request.user.is_superuser:
            ticket.delete()
            return redirect('home')
        return redirect('home')

    return render(request, 'app/ticket_delete.html', {'ticket': ticket})


@login_required
def ticket_s_review(request, id):
    ticket = models.Ticket.objects.get(id=id)
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            ticket.have_review = True
            ticket.save()
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
        'ticket': ticket,
    }
    return render(request, 'app/ticket_s_review.html', context=context)


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
            ticket.have_review = True
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
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
        if request.user == review.user or request.user.is_superuser:
            form = forms.ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('home')
        return redirect('home')    
    else:
        form = forms.ReviewForm(instance=review)

    return render(request, 'app/review_update.html', {'form': form,
                                                      'ticket': review.ticket})


@login_required
def review_delete(request, id):
    review = models.Review.objects.get(id=id)
    ticket = review.ticket

    if request.method == 'POST':
        if request.user == review.user or request.user.is_superuser:
            ticket.have_review = False
            ticket.save()
            review.delete()
            return redirect('home')
        return redirect('home')

    return render(request, 'app/review_delete.html', {'review': review})


@login_required
def subscription(request):
    followed_users = request.user.following.all()
    user_followers = request.user.followed_by.all()
    user_search_form = forms.UserSearchForm()  # Créez une instance du formulaire

    if request.method == 'POST':
        user_search_form = forms.UserSearchForm(request.POST)
        if user_search_form.is_valid():
            search_query = user_search_form.cleaned_data[
                'username_search'].strip()
            if search_query:
                users_found = User.objects.filter(
                    username__icontains=search_query
                ).exclude(pk=request.user.pk)
            else:
                users_found = User.objects.none()

            context = {
                'users_found': users_found,
                'followed_users': followed_users,
                'user_search_form': user_search_form,
                'user_followers': user_followers
            }
            print(context)

            return render(request, 'app/subscription.html', context=context)
    print(user_followers)
    return render(request, 'app/subscription.html', {
        'followed_users': followed_users,
        'user_search_form': user_search_form,
        'user_followers': user_followers})


@login_required
def follow_user(request, user_id):
    followed_user = get_object_or_404(User, pk=user_id)
    request.user.follow(followed_user)
    return redirect('subscription')


@login_required
def unfollow_user(request, user_id):
    followed_user = get_object_or_404(User, pk=user_id)
    request.user.unfollow(followed_user)
    return redirect('subscription')
