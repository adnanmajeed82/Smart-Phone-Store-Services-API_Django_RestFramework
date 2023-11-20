from django.urls import path
from .views import (
    SmartphoneListCreateView, SmartphoneDetailView,
    OrderListCreateView, OrderDetailView,
    BillListCreateView, BillDetailView,
    ReceiptListCreateView, ReceiptDetailView
)

urlpatterns = [
    path('smartphones/', SmartphoneListCreateView.as_view(), name='smartphone-list'),
    path('smartphones/<int:pk>/', SmartphoneDetailView.as_view(), name='smartphone-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('bills/', BillListCreateView.as_view(), name='bill-list'),
    path('bills/<int:pk>/', BillDetailView.as_view(), name='bill-detail'),
    path('receipts/', ReceiptListCreateView.as_view(), name='receipt-list'),
    path('receipts/<int:pk>/', ReceiptDetailView.as_view(), name='receipt-detail'),
]
