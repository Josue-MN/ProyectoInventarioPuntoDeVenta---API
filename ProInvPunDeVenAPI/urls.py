from django.urls import path
from django.contrib import admin
from ProInvPunDeVenAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bodegas/', views.BodegasList.as_view()),
    path('bodegas/<int:pk>', views.BodegasDetail.as_view())
]