from flask import Flask, render_template
import flask
import index
import pickle
import os
import dash
import dash_bootstrap_components as dbc

server = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
cf_port = os.getenv("PORT")

# app = dash.Dash(__name__, 
#                 external_stylesheets=[dbc.themes.BOOTSTRAP], 
#                 meta_tags=[{"name": "viewport", "content": "width=device-width"}],
#                 suppress_callback_exceptions=True,
# 				server=server,
# 				serve_locally = False)


app = dash.Dash(
    __name__,
	external_stylesheets=[dbc.themes.BOOTSTRAP], 
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    server=server
)

#---------------- Home ----------------#
@server.route("/")
def home():
	return render_template('index.html')


#---------------- Dash ----------------#
@server.route("/dash")
def getDash():
	return app.index()
    # return app.index()
	# return flask.redirect('/index')

#---------- ML Model endpoint ----------#
@server.route("/predictEcoFootprint")
def getPrediction():
	filename = "random_forest.pickle"
	loaded_model = pickle.load(open(filename, "rb"))

	T = [[-0.186135, -0.167322, 211, -0.183676, 0, 0, 0, 0, 0, 1],
    [-0.111125, -0.977002, 211, -0.903476, 0, 0, 0, 0, 0, 1]]
	y_pred = loaded_model.predict(T)

	return str(y_pred)


if __name__ == '__main__':
    # app.run()
	if cf_port is None:
		server.run(host='0.0.0.0', port=5000, debug=True)
	else:
		server.run(host='0.0.0.0', port=int(cf_port), debug=True)
    