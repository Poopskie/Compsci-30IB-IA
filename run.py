#-------------------------------------
#  Initials: JC
#  Program:  run.py
#  Class:    Compsci 30-IB
#  Function: Webapp Backend
# ------------------------------------
# Package runner
# runs all other files in folder "flaskapp"

from flaskapp import app

if __name__ == "__main__":
    app.run(debug=True)


