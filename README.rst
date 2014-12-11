django-fence
============

This is a simple Django app with middleware to block access (in a
user-friendly, but not particularly secure way) to early beta or testing sites.

The middleware checks for the presence of a session token. If it matches the
token specified in settings, the request procedes normally; if it doesn't,
the middleware displays a "please enter the token" form instead.  A single
token is shared for all authorized viewers.

The point is not to provide high security, but to instead prevent casual
visitors and crawlers from poking around a beta or testing site, while at the
same time making it *super easy* to give access to designers and people of
varying computer literacy.  You just have to tell them:  "Oh, the magic word is
'fiddlesticks'", and they can instantly get access without having to do any
sort of registration.  The goal is to be nicer user experience than HTTP basic
auth for this purpose.

Installation
~~~~~~~~~~~~

Get it into your path.  This ought to work::

    pip install -e http://github.com/yourcelf/django-fence.git

Usage
~~~~~

1. Add ``fence`` to ``INSTALLED_APPS``::

    INSTALLED_APPS += ('fence',)

2. Add middleware::

    MIDDLEWARE_CLASSES += ("fence.middleware.Fence",)

3. Define the magic word::

    FENCE_TOKEN = "secret"
    
4. Create a template to display in ``fence/say_the_magic_word.html``.  An example template::

    {% extends "base.html" %}

    {# Add a class to <body> which lets us hide footers/headers/etc. #}
    {% block body_class %}front-gate{% endblock %}

    {% block content %}

        <form method='post' action=''>{% csrf_token %}
            <p>We're still in beta.  What's the magic word?</p>
            {{ form }}
            <input type='submit' value='Let me in!' />
        </form>

    {% endblock %}

License
~~~~~~~

MIT License.

Copyright (C) 2012 Charlie DeTar

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Authors
~~~~~~~

By Charlie DeTar.
