from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import Payment
from users.serializers import PaymentSerializer
from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer

# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    serializer_class = PaymentSerializer
    filterset_fields = ("paid_course", "paid_lesson", "payment_method")
    ordering_fields = ("date",)
    permission_classes = (AllowAny,)

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

