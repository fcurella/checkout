from django.contrib import admin
from payments.models import PaymentRequest


class PaymentRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'amount_fmt', 'settled')
admin.site.register(PaymentRequest, PaymentRequestAdmin)
