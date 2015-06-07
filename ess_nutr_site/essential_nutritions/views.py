from django.shortcuts import render
from django.views.generic import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

def home_view(request):
    return render(request, 'home.html')

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        uname = request.POST.get('username', '')
        psword = request.POST.get('password', '')
        user = auth.authenticate(username=uname, password=psword)
        # if the user logs in and is active
        if user is not None and user.is_active:
            auth.login(request, user)
            # return redirect(home_view)
            return render(request, 'home.html')
        return render(request, 'login.html')


@login_required(redirect_field_name='login')
def logout_view(request):
    auth.logout(request)
    return render(request, 'home.html')
