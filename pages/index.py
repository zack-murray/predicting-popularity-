# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## What makes a hit song?
            
            Whether you're a self proclaimed music afficianato or just a casual listener, you've more
            than likely heard about the Billboard top charts. If not, Billboard is a magazine publication
            that since the 1940's has ranked and displayed the most popular songs in the United States.
            At the end of each year, Billboard compiles a chart of the 100 'hottest' songs, that are widely
            accepted as the standard for hit songs. 

            With this app you can explore the metrics that Spotify uses to diversify their songs. The
            model is based on data analyzing 10 years of Billboard charts from 2010 to 2019. Try altering
            the features to see if you can predict whether a song will be a hit!


            """
        ),
        dcc.Link(dbc.Button('Lets make a hit!', color='success'), href='/predictions')
    ],
    md=4,
)


column2 = dbc.Col(
    [
     html.Img(src='assets/spotify1.jpg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])