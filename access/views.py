from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from mixins.response import ExtendedJsonResponse
from mixins.auth import AuthMixin

# Create your views here.

@method_decorator(decorator=ensure_csrf_cookie, name="dispatch")
class SetCSRFToken(View):
    def get(self, request):
        return ExtendedJsonResponse()

class CheckUser(View, AuthMixin):
    """Kullanıcının oturum bilgilerini kontrol eder -> HEAD metoduna taşınabilir"""
    def get(self, request):
        # Varsayılan olarak anonim kullanici bilgileri doner
        # Ancak kullanıcı oturum acmissa oturum acan
        # kullanicinin email, corporate, is_active, is_superuser,
        # is_authenticated bilgilerini doner
        user = self.get_user_data(user=request.user)
        return ExtendedJsonResponse(data=user)

class AuthProcess(View, AuthMixin):
    """
    Bu view iki farkli endpointte iki farklı istegi karsilar
    
    path(route='login', view=views.AuthProcess.as_view()),
    path(route='logout', view=views.AuthProcess.as_view()),
    
    AuthMixin authentication_forum u dogrular message
    degiskenlerinden olusan sozluk veri tipi doner
    Errorsler interasyonla tek tek message icerisine girer
    """
    
    authentication_form = AuthenticationForm
    
    def get(self, request):
        """GET metodunda logout islemi yapilir"""
        result = self.logout_process(request=request)
        return ExtendedJsonResponse(**result)
    
    def post(self, request):
        """POST metodunda kullanici oturum acma islemi yapilir"""
        result = self.login_process(request=request)
        return ExtendedJsonResponse(**result)