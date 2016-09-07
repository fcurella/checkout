========
Checkout
========

Checkout is a small web app to receive payments or donations via Credit Card, powered by Stripe.

Configuration
=============

Fill in all your secrets in a ``.env`` file. See the ``env`` file (no initial dot) for a
list of the necessary secrets.

Installation
============

::

    $ pip install -r requirements.txt
    $ ./manage.py migrate
    $ ./manage.py collectstatic
    $ ./manage createsuperuser

Usage
=====

To create a payment request:

1. Go to ``/admin/payments/paymentrequest/add/`` and create a new payment.
2. Click on the 'View on site' link
3. Copy the URL from the address bar
4. Send the link to your recipient

To receive donations:

1. Create user accounts for your users at ``/admin/auth/user/add/`` 
2. Direct them to your website. Once logged in, they can use the 'Create a new payment' button.

License
=======

This software is relesed under the MIT License.
