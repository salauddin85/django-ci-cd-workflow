from django.urls import path
from .views import ItemListCreateAPIView, SingleItemDetailAPIView

urlpatterns = [
    path('items/', ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', SingleItemDetailAPIView.as_view(), name='item-detail')
]
