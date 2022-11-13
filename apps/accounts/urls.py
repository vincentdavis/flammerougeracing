from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
app_name = "accounts"


@method_decorator(csrf_exempt, name='dispatch')
class SignInView(TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        error = None
        try:
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                 login(request, user)
                 return HttpResponse("Login Success")
            else:
                error = 'Username or Password Incorrect'
        # No backend authenticated the credential
        except Exception as e:
            print("Exception", str(e))
        return HttpResponseRedirect(reverse('accounts:signin')+'#/signin?login=failed')

urlpatterns = [
    path("", SignInView.as_view(), name="signin"),

]
