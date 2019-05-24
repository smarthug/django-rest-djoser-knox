from django.conf.urls import url , include

from knox import views as knox_views
from knox_util.views import LoginView

urlpatterns = [
     url(r'login/', LoginView.as_view(), name='knox_login'),
     url(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     url(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]