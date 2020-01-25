from dash import Dash 
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd 

# Bootstrap CSS
css = ["https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"]

# Create an app through a Dash instance
app = Dash(__name__, external_stylesheets=css)

# Set contents of the html page
h1 = html.H1(children='Philippine Stock Market', className="display-4")
p = html.P(children='Summary of Stock Indices', className='lead')
hr = html.Hr(className="my-4")

# Read csv source
df = pd.read_csv('pseSectorSummaries2009-2019.csv')
# Get data values
date = list(df['Date'].unique())
psei_vals = list(df[df['Name'] == 'PSEi']['close'].copy())
all_shares_vals = list(df[df['Name'] == 'All Shares']['close'].copy())
financials_vals = list(df[df['Name'] == 'Financials']['close'].copy())
industrials_vals = list(df[df['Name'] == 'Industrials']['close'].copy())
holdings_vals = list(df[df['Name'] == 'HoldingFirms']['close'].copy())
property_vals = list(df[df['Name'] == 'Property']['close'].copy())
services_vals = list(df[df['Name'] == 'Services']['close'].copy())
mining_oil_vals = list(df[df['Name'] == 'MiningAndOil']['close'].copy())

# Data Visualization Setup
psei = {'x':date, 'y':psei_vals, 'type':'bar', 'name':'PSEi'}
all_shares = {'x':date, 'y':all_shares_vals, 'type':'bar', 'name':'All Shares'}
financials = {'x':date, 'y':financials_vals, 'type':'line', 'name':'Financials'}
industrials = {'x':date, 'y':industrials_vals, 'type':'line', 'name':'Industrials'}
holdings = {'x':date, 'y':holdings_vals, 'type':'line', 'name':'Holding Firms'}
properties = {'x':date, 'y':property_vals, 'type':'line', 'name':'Property'}
services = {'x':date, 'y':services_vals, 'type':'line', 'name':'Services'}
mining_oil = {'x':date, 'y':mining_oil_vals, 'type':'line', 'name':'Mining & Oil'}

viz = dcc.Graph(figure = {  'data':[psei, all_shares, financials, industrials, holdings, properties, services, mining_oil],
                            'layout':{'title': 'Dash Data Visualization'}
                            })

# Main div container
div_container = html.Div(children=[h1, p, hr, viz], className='jumbotron')

# Set layout of app
app.layout = html.Div(children=[div_container], className="container")

if __name__ == '__main__':
    app.run_server(debug=True)
