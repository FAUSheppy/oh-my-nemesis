
import flask
import smtplib

import jsonConfig as jc

pagesApi = flask.Blueprint('simple_page', __name__, template_folder='templates')

@pagesApi.route("/contact-api", methods=['POST'])
def contactAPI():
    
    email = flask.request.form["email"]
    name  = flask.request.form["name"]
    subject = "Subject: {} ({})\n\n".format(flask.request.form["subject"], name)
    message = subject + flask.request.form["message"]
    smtpTarget = smtplib.SMTP(jc.mainConfig().smtp)
    smtpTarget.sendmail(email, jc.mainConfig().target_email , message)
    smtpTarget.quit()

    return flask.redirect("/thanks")