from django import forms

from .models import PaymentRequest


class CreatePaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentRequest
        fields = (
            'amount',
            'currency',
            'title',
            'description'
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreatePaymentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(CreatePaymentForm, self).save(commit=False)
        obj.user = self.request.user
        if commit:
            obj.save()
            self.save_m2m()
        return obj
