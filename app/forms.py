from django import forms
from . import models
from authentication.models import User

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class UserSearchForm(forms.Form):
    username_search = forms.CharField(label='Rechercher des utilisateurs', max_length=100)
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError(u'Username "%s" ajouter au abonnement' % username)
    #     else:
    #         raise forms.ValidationError(u'Username "%s" n`existe pas' % username)
    #     return username
