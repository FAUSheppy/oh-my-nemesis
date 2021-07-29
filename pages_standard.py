import database as db
import jsonConfig as jc
import flask
import flask_login as fl
import os

standardPages = flask.Blueprint('standardPages', __name__, template_folder='templates')
@standardPages.route('/')
def index():
    '''Landing page/index page/root page'''

    user = db.getUserByFlaskLoginId(fl.current_user)
    return flask.render_template("standard/index.html", 
                services=jc.services(), 
                pricesSections=jc.pricesSections(),
                config=jc.mainConfig(),
                currentUser=user)

@standardPages.route("/dashboard")
@fl.login_required
def dashboard():
    '''Logged in user dashboard'''

    user = db.getUserByFlaskLoginId(fl.current_user)
    return flask.render_template("standard/user_dashboard.html",  
                config=jc.mainConfig(),
                currentUser=user)

@standardPages.route("/shop")
def shop():
    '''Shop to buy shit'''

    user = db.getUserByFlaskLoginId(fl.current_user)
    return flask.render_template("standard/shop.html",  
                config=jc.mainConfig(),
                currentUser=user)

@standardPages.route("/about")
def about():
    '''About Page'''

    user = db.getUserByFlaskLoginId(fl.current_user)
    return flask.render_template("standard/about.html", 
                    config=jc.mainConfig(), 
                    currentUser=user)

@standardPages.route("/impressum")
def impressum():
    '''About Page'''

    user = db.getUserByFlaskLoginId(fl.current_user)
    return flask.render_template("standard/impressum.html", 
                    config=jc.mainConfig(), 
                    currentUser=user)

@standardPages.route("/contact")
def contact():
    '''Contact Page'''

    offer = jc.getOfferById(flask.request.args.get("offerId"))
    user = db.getUserByFlaskLoginId(fl.current_user)

    return flask.render_template("standard/contact.html", 
                conf=jc.mainConfig(),
                currentUser=user, selectedOffer=offer)

@standardPages.route("/thanks")
def thanks():
    '''Post Contact thanks page'''

    user = db.getUserByFlaskLoginId(fl.current_user)
    return flask.render_template("standard/thanks.html", config=jc.mainConfig(), 
                currentUser=user)
