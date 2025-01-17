from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  
    path('shop/', views.shop, name='shop'),
    path('transaction_complete/<int:product_id>/', views.transaction_complete, name='transaction_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
