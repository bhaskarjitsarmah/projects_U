from flaskexample import app 

# Import the Python libraries. 
# We recommend sklearn's joblib function to load your model, 
# plotly for your dashboards, sqlalchemy for your database.
# You will need Flask functions as well.
import json
from flask import render_template, request, jsonify
from sklearn.externals import joblib
import plotly
from plotly.graph_objs import *
from sqlalchemy import create_engine

# Include other Python libraries you will use. 


# First, let's connect to the sqlite database you have created in the first part.
disk_engine = create_engine('sqlite:///Your_Database.db')

# Now, let's load your model. 
model = joblib.load("Your_Model.pkl")


# In the index webpage you should get user input texts to test in your model 
# and you should show some cool visualizations of the data. 

@app.route('/')
@app.route('/index')
def index():

  # First, read the data. You will need the data to create the visuals. 
  ##......

  # Then, extract what data that you will use to create the visuals. 
  ##......

  # Here, you can find a random visual as an example. You should understand the logic.
  # You should create your own visuals using the data. 

	graphs = [dict(
        data=[Bar(### for online use go.Bar instead
            x=['Apples', 'Oranges'],
            y=[5, 7]
        )],
        layout=dict(
            title='Bar Plot of Fruits',
            yaxis=dict(
                title="Count"
            ),
            xaxis=dict(
                title="Categories"
            )
        )
    )
    ]


  # Here we create the JSON file to store render the webpage. 
	ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
	graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)


  # This will render the master.html Please see that file.
	return render_template('master.html', ids = ids, graphJSON = graphJSON)


# Here, we handle the user query. 
@app.route('/go')
def go():
    # User input is saved in query. 
    query = request.args.get('query', '') 

    # Now, you should use your model to predict the label for the user query. 
    #....

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query = query,
        cat = result_class,
        recommend = recommend
    )
