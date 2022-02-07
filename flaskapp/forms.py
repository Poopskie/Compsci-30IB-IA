#-------------------------------------
#  Initials: JC
#  Program:  forms.py
#  Class:    Compsci 30-IB
#  Function: Webapp Backend
# ------------------------------------
# second divisions for forms submitted within the webapp
# part of the "flaskapp" package
# provides templates and inputs for forms that are sent to html files

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField
from wtforms.fields.datetime import DateField, DateTimeLocalField # using different fields for different html inputs
from wtforms.validators import DataRequired, Length, Email, Optional # built in validators to check user input

# flask_wtf automatically turns python classes into html forms

class EnglishCovid(FlaskForm): # wtforms allows me to use validators to make sure the form is filled
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)]) #DataRequired requires the form to be filled
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()]) # email automatically checks for a valid email
    # bunch of stuff for the form
    # Can use BooleanField for checkboxes 
    birth_date = DateField('Date of Birth', validators=[DataRequired()])
    PHN = StringField('Personal Health Number', validators=[DataRequired()])
    Hinfo1 = RadioField('Does this person have any allergies including allergies to any vaccine, medicine, or food?', 
                                                                        choices=['Yes', 'No'], validators=[DataRequired()])
    Hinfo1string = StringField('List any allergies:', validators=[Optional()])
    Hinfo2 = RadioField('Does this person have any chronic illness?', 
                                                                        choices=['Yes', 'No'], validators=[DataRequired()])
    Hinfo2string = StringField('List any chronic illnesses:', validators=[Optional()])
    Hinfo3 = RadioField('Is this person taking any medicine?', 
                                                                        choices=['Yes', 'No'], validators=[DataRequired()])
    Hinfo3string = StringField('List any medications:', validators=[Optional()])
    Hinfo4 = RadioField('Is this person pregnant?', choices=['Yes', 'No'], validators=[DataRequired()])
    Hinfo5 = RadioField('Is this person breastfeeding?', choices=['Yes', 'No'], validators=[DataRequired()])
    Hinfo6 = RadioField('Has this person had COVID-19 vaccine before?', 
                                                                        choices=['Yes', 'No'], validators=[DataRequired()])
    Hinfo6date = DateField('Date of vaccine:', validators=[Optional()])
    Hinfo7 = RadioField('Has this person ever had a side effect from COVID-19 immunzation?', 
                                                                        choices=['Yes', 'No'], validators=[DataRequired()])
    Hinfo7string = StringField('Side effects:', validators=[Optional()])
    Hinfo8 = RadioField('Will this person get another vaccine in the 14 days before they get the COVID-19 vaccine?', 
                                                                        choices=['Yes', 'No'], validators=[DataRequired()])
    Hinfo8string = StringField('Other vaccines:', validators=[Optional()])

    consentgiver = StringField('Name of person giving consent:', validators=[DataRequired()])
    phone = StringField('Phone Number: ', validators=[DataRequired()])
    relationshipto = SelectField('Relationship to person being immunized:', 
        choices=['Person being immunized', 'Parent (with legal authority to consent)', 'Guardian/Legal representative', 'Co-decision-maker',
                    'Specific decision-maker', 'Agent'], validators=[DataRequired()])
    signature = StringField('Please Sign initials:', validators=[DataRequired(), Length(min=2)])


    submit = SubmitField('Submit')







