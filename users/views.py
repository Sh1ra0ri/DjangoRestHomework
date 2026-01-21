from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from users.models import Payment
from users.serializers import PaymentSerializer


# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    serializer_class = PaymentSerializer
    filterset_fields = ("paid_course", "paid_lesson", "payment_method")
    ordering_fields = ("date",)
