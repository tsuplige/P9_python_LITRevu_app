from django import forms
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = (
        (1, "One"),
        (2, "Two"),
        (3, "Three"),
        (4, "Four"),
        (5, "Five"),
    )

    rating = forms.ChoiceField(choices=RATING_CHOICES, label="Rating")

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class UserSearchForm(forms.Form):
    username_search = forms.CharField(label='Rechercher des utilisateurs',
                                      max_length=100)
