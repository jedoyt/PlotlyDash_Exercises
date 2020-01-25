from dash import Dash 
import dash_core_components as dcc 
import dash_html_components as html 

# Bootstrap CSS
css = ["https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"]

# Create an app through a Dash instance
app = Dash(__name__, external_stylesheets=css)

# Set contents of the html page
h1 = html.H1(children='Hello Dash', className="display-4")
p = html.P(children='Dash: A web application framework for Python', className='lead')
hr = html.Hr(className="my-4")

# Data Visualization Setup
san_francisco_data = {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'San Francisco'}
montreal_data = {'x':[1,2,3], 'y':[2,4,5], 'type':'bar', 'name':u'Montréal'}
viz = dcc.Graph(figure = {  'data':[san_francisco_data, montreal_data],
                            'layout':{'title': 'Dash Data Visualization'}
                            })

# Main div container
div_container = html.Div(children=[h1, p, hr, viz], className='jumbotron')

# Set layout of app
app.layout = html.Div(children=[div_container], className="container")

if __name__ == '__main__':
    app.run_server(debug=True)
