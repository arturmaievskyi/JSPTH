from flask.templating import render_template
from abc import ABC, abstractmethod



@abstractmethod
def render_about():
    return render_template("about.html")


@abstractmethod
def render_contact():
    return render_template('contact.html')


@abstractmethod
def render_support():
    return render_template('support_me.html')