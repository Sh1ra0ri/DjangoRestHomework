from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import (create_stripe_price, create_stripe_product,
                            create_stripe_session)


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


class StripePaymentCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        course_id = request.data.get("course_id")
        course = get_object_or_404(Course, id=course_id)

        product = create_stripe_product(course.title)
        price = create_stripe_price(course.price, product.id)
        session = create_stripe_session(price.id)

        payment = Payment.objects.create(
            user=request.user,
            paid_course=course,
            total=course.price,
            payment_method="Stripe",
            session_id=session.id,
            link=session.url,
            status="pending",
        )

        return Response({"payment_link": session.url}, status=status.HTTP_201_CREATED)
