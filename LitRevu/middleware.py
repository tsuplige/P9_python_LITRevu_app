from django.http import HttpResponseRedirect
from django.urls import reverse


# class RedirectAuthenticatedUserMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(reverse('home'))
#         response = self.get_response(request)
#         return response
