
from django.contrib import admin
from django.urls import path,include
from .import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('store.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
