from django.urls import path
from .views import CelularesView, ContatoView, IndexView, detalhes_celular, ManutencaoView, cadastro
from django.contrib.auth import views
from aplic.forms import UserLoginForm
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('detalhes_celular/<int:celular_id>/', detalhes_celular, name='detalhes'),
    path("contato", ContatoView.as_view(), name="contato"),
    path("celulares", CelularesView.as_view(), name="celulares"),
    path("manuntencao", ManutencaoView.as_view(), name="manuntencao"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path("cadastro/", cadastro, name="cadastro")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()