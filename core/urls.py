from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/concursos/', permanent=False), name='home'),
    path('accounts/', include('apps.accounts.urls')),
    path('candidatos/', include('apps.candidatos.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('concursos/', include('apps.concursos.urls')),
    path('candidaturas/', include('apps.candidaturas.urls')),
    path('pagamentos/', include('apps.pagamentos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
