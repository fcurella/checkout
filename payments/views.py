import datetime
import pytz
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView

from payments.models import PaymentRequest
from payments.forms import CreatePaymentForm

import stripe
# Create your views here.
# set your secret key: remember to change this to your live secret key in production
# see your keys here https://manage.stripe.com/account
stripe.api_key = settings.STRIPE_API_KEY


class PaymentCreate(CreateView):
    model = PaymentRequest
    form_class = CreatePaymentForm

    def get_form_kwargs(self):
        kwargs = super(PaymentCreate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaymentCreate, self).dispatch(*args, **kwargs)


class PaymentList(ListView):
    model = PaymentRequest

    def get_queryset(self):
        if self.request.user.is_superuser:
            return PaymentRequest.objects.all()
        return PaymentRequest.objects.filter(user=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaymentList, self).dispatch(*args, **kwargs)


class PaymentDetail(DetailView):
    model = PaymentRequest

    def get_queryset(self):
        if self.request.user.is_superuser:
            return PaymentRequest.objects.all()
        return PaymentRequest.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        ctx = super(PaymentDetail, self).get_context_data(*args, **kwargs)
        ctx.update({
            'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY
        })
        return ctx

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaymentDetail, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        # get the credit card details submitted by the form
        token = request.POST['stripe_token']

        payment_request = self.get_object()
        try:
            # create the charge on Stripe's servers - this will charge the user's card
            stripe.Charge.create(
                amount=int(payment_request.amount * 100),  # amount in cents, again
                currency=payment_request.currency.lower(),
                card=token,
                description=payment_request.description
            )
            messages.success(request, 'Payment Successful.')
            payment_request.settled = True
            payment_request.paid_on = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
            payment_request.save()
            return HttpResponseRedirect(payment_request.get_absolute_url())

        except stripe.CardError as e:
            messages.error(request, e)

        return super(PaymentDetail, self).get(request, *args, **kwargs)
