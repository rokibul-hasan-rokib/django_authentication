from django.shortcuts import redirect
from django.http import HttpResponseForbidden

class AdminOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info

        if path.startswith('/dashboard/'):
            if not request.user.is_authenticated:
                return redirect('login') 

            if not request.user.groups.filter(name='Admin').exists():
                return HttpResponseForbidden("Access denied: Admins only")

        return self.get_response(request)
