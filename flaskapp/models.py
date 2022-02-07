#-------------------------------------
#  Initials: JC
#  Program:  routes.py
#  Class:    Compsci 30-IB
#  Function: Webapp Backend
# ------------------------------------
# file for db models 

from datetime import datetime # using datetime for time logs
from flaskapp import db # importing from the package

class Consentform(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for each person
    date_created = db.Column(db.DateTime(), default=datetime.utcnow) # logs anytime an instance of the class is created

    # below is all part of EnglishCovid objects
    first_name = db.Column(db.String(200), nullable=False) # don't allow user to input nothing
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    birth_date = db.Column(db.Date(), nullable=False) # DateField stores as a datetime.date object
    PHN = db.Column(db.String(200), nullable=False)
    Hinfo1 = db.Column(db.String(200), nullable=False)
    Hinfo1string = db.Column(db.String(200))
    Hinfo2 = db.Column(db.String(200), nullable=False)
    Hinfo2string = db.Column(db.String(200))
    Hinfo3 = db.Column(db.String(200), nullable=False)
    Hinfo3string = db.Column(db.String(200))

    Hinfo4 = db.Column(db.String(200), nullable=False)
    Hinfo5 = db.Column(db.String(200), nullable=False)

    Hinfo6 = db.Column(db.String(200), nullable=False)
    Hinfo6date = db.Column(db.Date(), default=datetime.utcnow)
    Hinfo7 = db.Column(db.String(200), nullable=False)
    Hinfo7string = db.Column(db.String(200))
    Hinfo8 = db.Column(db.String(200), nullable=False)
    Hinfo8string = db.Column(db.String(200))
    
    consentgiver = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(200), nullable=False)
    relationshipto = db.Column(db.String(200), nullable=False)
    signature = db.Column(db.String(200), nullable=False)

    pdf = db.Column(db.Boolean(), default=False) 
    # helps with sorting so I don't make duplicate pdfs
    

    def __repr__(self): # output the object as a string 
        return '<Form %r>' % self.id