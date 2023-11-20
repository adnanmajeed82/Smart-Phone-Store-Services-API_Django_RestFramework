from rest_framework import generics
from .models import Smartphone, Order, Bill, Receipt
from .serializers import SmartphoneSerializer, OrderSerializer, BillSerializer, ReceiptSerializer

class SmartphoneListCreateView(generics.ListCreateAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer

class SmartphoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class ReceiptListCreateView(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

class ReceiptDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
