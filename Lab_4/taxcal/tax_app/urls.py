from django.urls import path
from . import views
urlpatterns = [
    path('', views.default_view, name='default'),
    path('<int:number>/', views.anyNumber, name='anyNumber'),
    path('taxrate/', views.tax_rate_view, name='tax_rate'),
]
