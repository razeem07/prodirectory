from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('add/', views.ProductCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
]