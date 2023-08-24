from django.contrib import admin
from django.urls import path
import authentication.views
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),

    path('home/', app.views.home, name='home'),

    path('ticket/', app.views.ticket, name='ticket'),
    path('ticket/<int:id>/change/', app.views.ticket_update, name='ticket-update'),

    path('critique/', app.views.critique, name='critique'),
    path('critique/<int:id>/change/', app.views.critique_update, name='critique-update'),

    path('abonnements/', app.views.subscription, name='subscription'),

]
