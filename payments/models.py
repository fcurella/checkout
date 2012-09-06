import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from markupfield.fields import MarkupField
# Create your models here.


CURRENCY_CHOICES = (
    ('USD', 'USD'),
    ("EUR", 'EUR'),
)


class PaymentRequest(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(blank=True, max_length=100)
    description = MarkupField(blank=True, markup_type='markdown')
    amount = models.FloatField()
    currency = models.CharField(max_length=3, default='USD', choices=CURRENCY_CHOICES)
    settled = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    paid_on = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now)

    def __unicode__(self):
        return u"%s - %s" % (self.title, self.amount_fmt())

    def get_absolute_url(self):
        return reverse('payment_detail', kwargs={'pk': self.id})

    def amount_fmt(self):
        return u"%s %.2f" % (self.currency, self.amount)
    amount_fmt.short_description = u'amount'
