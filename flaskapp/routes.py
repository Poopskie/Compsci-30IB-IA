#-------------------------------------
#  Initials: JC
#  Program:  routes.py
#  Class:    Compsci 30-IB
#  Function: Webapp Backend
# ------------------------------------
# file for routes on the webapp

from flask import render_template, url_for # render and url used in html for front end
from flask import request, redirect # redirect only used in routes was moved from previous app.py
from werkzeug.utils import redirect 

# import classes from "forms.py" and "models.py" which are in my package flaskapp
from flaskapp import app, db
from flaskapp.forms import EnglishCovid
from flaskapp.models import Consentform



@app.route("/", methods=['POST', 'GET']) # Using HTTP method POST to send data to the db
def index(): # block for html
    return render_template("index.html", consent_form= Consentform)

# secondary sublink for english covid-19 copied for other links
@app.route("/englishcovid19", methods= ['GET', 'POST'])
def englishcovid19():
    form = EnglishCovid() # using class imported from models.py
    if form.validate_on_submit(): # only redirects and adds to database if valid
        new_form = Consentform(first_name = form.first_name.data, last_name = form.last_name.data
            , email = form.email.data, birth_date = form.birth_date.data, PHN = form.PHN.data
            , Hinfo1 = form.Hinfo1.data, Hinfo1string = form.Hinfo1string.data, Hinfo2 = form.Hinfo2.data, Hinfo2string = form.Hinfo2string.data
            , Hinfo3 = form.Hinfo3.data, Hinfo3string = form.Hinfo3string.data, Hinfo4 = form.Hinfo4.data, Hinfo5 = form.Hinfo5.data
            , Hinfo6 = form.Hinfo6.data, Hinfo6date = form.Hinfo6date.data, Hinfo7 = form.Hinfo7.data, Hinfo7string = form.Hinfo7string.data
            , Hinfo8 = form.Hinfo8.data, Hinfo8string = form.Hinfo8string.data, consentgiver = form.consentgiver.data, phone = form.phone.data
            , relationshipto = form.relationshipto.data, signature = form.signature.data) 
            # inserting form data after post into db model

        
        db.session.add(new_form) # creates new user only after inputing name
        db.session.commit()
        # runs only after successful submission
        return redirect(f"/confirmation/{new_form.id}") # send to confirmation page

    # if form isn't submmited yet or invalid continue to render englishcovid19
    return render_template("englishcovid19.html", form=form) # passing in parameter "form"

# final confirmation page
@app.route("/confirmation/<int:id>") # website render as form id to avoid duplicates
def confirmation(id):
    return render_template("confirmation.html", id=id) # passing in parameter "id"


@app.route("/mandarincovid19")
def mandarincovid19():
    pass


