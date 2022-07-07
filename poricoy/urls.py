from django.contrib import admin
from django.urls import path, include
from register import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name='register'),
    path('', include('main.urls')),
    path('login/', v.login_form, name='login'),
    path('p/', include('portfolio.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
