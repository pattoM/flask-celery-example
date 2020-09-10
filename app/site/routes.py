from flask import Flask, jsonify, request, abort, redirect, url_for, render_template, flash, Blueprint, session
import json
from uuid import uuid4
from datetime import datetime, timedelta
from .forms import *
from .. import app
from ..models import *


#site blueprint
site = Blueprint('site', __name__ , template_folder='templates')



@site.route('/', methods=['GET','POST'])
def index():
    """
    Single page to collect emails for them to be emailed a video link to a programming question 
    """
    form = EmailSignupForm()

    if form.validate_on_submit():
        try:
            user_ip = request.remote_addr
            user_browser = request.headers.get('User-Agent',None)

            new_email = Emails(email=form.email.data, signup_ip=user_ip, signup_browser=user_browser) 
            db.session.add(new_email)
            db.session.commit() 
            flash("You have successfully signed up on the email list.", "alert-success")
            return redirect(url_for('site.index'))
        except Exception as e:
            print(e)

            flash("An error occurred :( Try again or use another email.", "alert-danger")
            return redirect(url_for("site.index"))

    

    return render_template('site/index.html', form=form)

