from django.contrib import admin
from django.urls import path
import authentication.views
import app.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),

    path('home/', app.views.home, name='home'),

    path('ticket/upload', app.views.ticket_upload, name='ticket-upload'),
    path('ticket/<int:id>/change/', app.views.ticket_update, name='ticket-update'),
    path('ticket/<int:id>/delete/', app.views.ticket_delete, name='ticket-delete'),
    path('ticket/<int:id>/review/upload', app.views.ticket_answer, name='ticket-answer'),

    path('review/upload', app.views.review_upload, name='review-upload'),
    path('review/<int:id>/change/', app.views.review_update, name='review-update'),
    path('review/<int:id>/delete/', app.views.review_delete, name='review-delete'),

    path('abonnements/', app.views.subscription, name='subscription'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
