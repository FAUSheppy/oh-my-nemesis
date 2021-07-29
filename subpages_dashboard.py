import jsonConfig as jc
import flask
import flask_login as fl
import database as db
import collections
import os

subpagesDashboard = flask.Blueprint('subpagesDashboard', __name__, template_folder='templates')

@subpagesDashboard.route("/dashboard/self-analysis")
@fl.login_required
def selfMatchHistory():
    user = db.getUserByFlaskLoginId(fl.current_user)
    return flask.render_template("dashboardSubpages/self_analysis.html", 
                                    config=jc.mainConfig(), 
                                    currentUser=user,
                                    champs=jc.champs())

@subpagesDashboard.route("/dashboard/self_matchups")
@fl.login_required
def selfMatchups():
    user = db.getUserByFlaskLoginId(fl.current_user)
    return flask.render_template("dashboardSubpages/self_matchups.html", 
                    config=jc.mainConfig(), currentUser=user, champs=jc.champs())

@subpagesDashboard.route("/dashboard/team-match-history")
@fl.login_required
def teamMatchHistory():
    user = db.getUserByFlaskLoginId(fl.current_user)
    return flask.render_template("dashboardSubpages/subpage_team_history.html", 
                    config=jc.mainConfig(), currentUser=user, champs=jc.champs())

@subpagesDashboard.route("/team_champselect", methods=['GET', 'POST'])
@fl.login_required
def teamChampSelect():
    teamid = "example"

    roles = collections.OrderedDict()
    roles["Top"] = None
    roles["Jungle"] = None
    roles["Mid"] = None
    roles["Bottom"] = None
    roles["Support"] = None

    if flask.request.method == "POST":
        role   = flask.request.args.get("role")
        champ  = flask.request.args.get("champ")
        action = flask.request.args.get("action")
        
        if action == "remove":
            db.teamChampSelectRemove(teamid, champ, role)
        elif action == "add":
            db.teamChampSelectAdd(teamid, champ, role)
        else:
            flask.abort(500)

        return ("", 204)

        

    for key in roles:
        path = "config/teams/{}/roles/{}.json".format(teamid, key)
        if not os.path.isfile(path):
            with open(path, "w") as  f:
                f.write('{ "champions": [] }')
        roles[key] = jc.readJsonFile(path)

    allChampions = jc.readJsonDir("config/champions")

    return flask.render_template("team_champselect.html", roles=roles,
                        allChampions=allChampions, config=jc.readJsonFile("config/config.json"), currentUser=fl.current_user)

@subpagesDashboard.route("/team_composition_overview")
@fl.login_required
def teamCompositionOverview():
    username = fl.current_user
    user = jc.readJsonFile(os.path.join("data/users/", "{}.json".format(username)))
    teamComps = jc.readJsonDir(os.path.join("config/teams/{}/compositions/".format("example")))
    return flask.render_template("team_composition_overview.html", config=jc.readJsonFile("config/config.json"), currentUser=fl.current_user,
                                        userInDatabase=user, teamComps=teamComps)

@subpagesDashboard.route("/team_composition_single")
@fl.login_required
def teamCompositionSingle():
    roles = collections.OrderedDict()
    roles["Top"] = None
    roles["Jungle"] = None
    roles["Mid"] = None
    roles["Bottom"] = None
    roles["Support"] = None
    allChampions = jc.readJsonDir("config/champions")
    return flask.render_template("team_composition_single.html", roles=roles,
                                    teamChamps=allChampions,
                                    config=jc.readJsonFile("config/config.json"),
                                    currentUser=fl.current_user)
    
