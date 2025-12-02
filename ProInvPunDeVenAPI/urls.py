from django.urls import path
from django.contrib import admin
from ProInvPunDeVenAPI import views

urlpatterns = [
    path('bodegas/', views.BodegasList.as_view()),
    path('bodegas/<int:pk>', views.BodegasDetail.as_view()),
    path('cargos/', views.CargosList.as_view()),
    path('cargos/<int:pk>', views.CargosDetail.as_view())
]