#-------------------------------------
#  Initials: JC
#  Program:  pdf.py
#  Class:    Compsci 30-IB
#  Function: Webapp Backend
# ------------------------------------
# file for conversion to pdf
# referenced "Chart Explorers" youtube videos for help

from fpdf import FPDF

# required files and libraries to get data from database
from flaskapp import db
from flaskapp.models import Consentform

num = input("How many pdfs to go through? ")

# goes through user specified top bound
for i in range(int(num)): # breaks when all consentforms have a true pdf value
    form = Consentform.query.order_by(Consentform.pdf).first() # orders by those that are False
    if form.pdf == False: # check to avoid duplicates

        # creating pdf template/class
        pdf = FPDF('P', 'in', 'Letter') # specifying format
        # P for portrait, mm for measurement, and letter for pdf size

        pdf.add_page() # creating first page

        pdf.set_auto_page_break(auto=True, margin=0.75) # set bottom and top margin to 0.75in
        #setting font -> times, normal, 12pt
        pdf.set_font('times', '', 12)

        pdf.cell(0,0.25, f"Form ID: {form.id}" , ln = True)
        pdf.cell(0,0.25, f"Date Created: {form.date_created}" , ln = True)

        pdf.cell(0,0.25, f"First Name: {form.first_name.title()}" , ln = True)
        pdf.cell(0,0.25, f"Last Name: {form.last_name.title()}" , ln = True)
        pdf.cell(0,0.25, f"Email: {form.email}" , ln = True)
        pdf.cell(0,0.25, f"Birth Date: {form.birth_date}" , ln = True)
        pdf.cell(0,0.25, f"Personal Health Number: {form.PHN}" , ln = True)
        pdf.cell(0,0.25, ln=True)

        pdf.cell(0,0.25, f"Does this person have any allergies including allergies to any vaccine, medicine, or food?: {form.Hinfo1}" , ln = True)
        pdf.cell(0,0.25, f"Allergies: {form.Hinfo1string}" , ln = True)
        pdf.cell(0,0.25, ln=True)
        pdf.cell(0,0.25, f"Does this person have any chronic illness?: {form.Hinfo2}" , ln = True)
        pdf.cell(0,0.25, f"Illnesses: {form.Hinfo2string}" , ln = True)
        pdf.cell(0,0.25, ln=True)
        pdf.cell(0,0.25, f"Is this person taking any medicine?: {form.Hinfo3}" , ln = True)
        pdf.cell(0,0.25, f"Medications: {form.Hinfo3string}" , ln = True)
        pdf.cell(0,0.25, ln=True)

        pdf.cell(0,0.25, f"Is this person pregnant?: {form.Hinfo4}" , ln = True)
        pdf.cell(0,0.25, f"Is this person breastfeeding?: {form.Hinfo5}" , ln = True)
        pdf.cell(0,0.25, ln=True)

        pdf.cell(0,0.25, f"Has this person had COVID-19 vaccine before?: {form.Hinfo6}" , ln = True)
        pdf.cell(0,0.25, f"Date of past vaccine: {form.Hinfo6date}" , ln = True)
        pdf.cell(0,0.25, ln=True)
        pdf.cell(0,0.25, f"Has this person ever had a side effect from COVID-19 immunzation?: {form.Hinfo7}" , ln = True)
        pdf.cell(0,0.25, f"Side Effects: {form.Hinfo7string}" , ln = True)
        pdf.cell(0,0.25, ln=True)
        pdf.cell(0,0.25, f"Will this person get another vaccine in the 14 days before they get the COVID-19 vaccine?: {form.Hinfo8}" , ln = True)
        pdf.cell(0,0.25, f"Other Vaccines: {form.Hinfo8string}" , ln = True)

        pdf.cell(0,0.25, ln=True)
        pdf.cell(0,0.25, f"Name of person giving consent: {form.consentgiver}" , ln = True)
        pdf.cell(0,0.25, f"Phone Number: {form.phone}" , ln = True)
        pdf.cell(0,0.25, f"Relationship to person being immunized: {form.relationshipto}" , ln = True)
        pdf.cell(0,0.25, f"Signed Initials: {form.signature}" , ln = True)




        # final step to output pdf, named accoding to my client's needs
        pdf.output(f"{form.last_name.title()}, {form.first_name.title()} consent form.pdf")

        Consentform.query.order_by(Consentform.pdf).first().pdf = True # orders by false first
        db.session.commit() # change value of the converted form's pdf value to true

    else:
        print(f"{i} forms have been converted into pdfs")
        break
else: # if for loop executes normally
    print(f"{num} forms have been converted into pdfs")




