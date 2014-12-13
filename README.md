Flask-iMail
===========

Flask integration for Mailgun mail service, from my own point of view.

# Installation

I would advise you to create first a virtual environment and then
install the library

    $ git clone https://github.com/ipinak/Flask-iMail.git
    $ cd Flask-iMail
    $ python setup.py build install

If you have executed the above and you didn't face any error you will
be ready to use the library.


# Integration

    from flask import Flask
    import mailgun

    app = Flask(__name__)
    mailgun = mailgun.Mailgun()
    app.config['MAILGUN_KEY'] = 'your-key'
    app.config['DOMAIN'] = 'your-domain'
    mailgun.init_app(app)

    # Send an email
    mailgun.send_email('sender@gmail.com', 'receiver@gmail.com',
    message='test1', subject='test subject')


# Tests

If you want to verify the ALL of the tests you need to open the file
tests.py and set your **MAILGUN_KEY** and **DOMAIN** as well as the
sender and receiver. Otherwise you will face an error stating:
***Exception: wrong result back...***

If you do changes then run

    $ python tests.py
