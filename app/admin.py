from django.contrib import admin
from app.models import Ticket, Review
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'time_created')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'user', 'ticket', 'time_created')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
