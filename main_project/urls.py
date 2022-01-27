
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main_api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.ShowAddCars.as_view()),
    path('', views.Home.as_view()),
    path('rate/', views.AddRates.as_view()),
    path('cars/<int:id>', views.DeleteCar.as_view()),
    path('popular/', views.ShowPopular.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)