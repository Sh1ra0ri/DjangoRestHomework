import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_stripe_product(name):
    product = stripe.Product.create(name=name)
    return product

def create_stripe_price(amount, product_id):
    price = stripe.Price.create(
        unit_amount=int(amount * 100),
        currency='rub',
        product=product_id,
    )
    return price

def create_stripe_session(price_id):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/success/",
        cancel_url="http://127.0.0.1:8000/cancel/",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session