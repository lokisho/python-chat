from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/', include('uniauth.urls', namespace='uniauth')),
    path('', include('chat.urls')),
]
