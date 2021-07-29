
import flask
import flask_login as fl
import database as db
import jsonConfig as jc

pagesLoginManagement = flask.Blueprint('pagesLoginManagement', __name__, template_folder='templates')

@pagesLoginManagement.route("/login", methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        print(username, password)
        acceptedUser = db.safeCheckLogin(username, password)
        if acceptedUser:
            fl.login_user(acceptedUser)
            return flask.redirect(flask.url_for("standardPages.dashboard"))
        else:
            return flask.abort(401)
    else:
        return flask.render_template("standard/login.html", 
                    config=jc.mainConfig())

@pagesLoginManagement.route("/logout")
@fl.login_required
def logout():
    fl.logout_user()
    return flask.redirect("/")
