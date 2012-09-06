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

License
=======

This software is relesed under the MIT License.
