# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np 
import pandas as pd 

# Imports from this application
from app import app

# Load pipeline
from joblib import load
pipeline = load('assets/RFRpipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.Br(),
        html.Br(),
        dcc.Markdown(
            """

        
        
            **Instructions**: Play with the features to see if you can predict a hit song!
            """,
            style={
                'textAlign': 'center',
                'fontSize': 18
            }
        ), 
        dcc.Markdown(
            """

                            Spotify Track Properties


            * **Accousticness** - The higher the value the more acoustic the song is. 
            * **Beats_per_minute** - The tempo of the song.
            * **Danceability** - The higher the value, the easier it is to dance to this song.
            * **Energy** - The energy of a song - the higher the value, the more energtic the song is.
            * **Length** - The duration of the song (in seconds).
            * **Liveness** - The higher the value, the more likely the song is a live recording.
            * **Loudness(dB)** - The higher the value, the louder the song.
            * **Speechiness** - The higher the value the more spoken word the song contains.
            * **Valence** - The higher the value, the more positive mood for the song. 
            * **Year of hit** - The release year of the recording. 
            * **Genre** - The genre of the track 

            """,
            style={
                'lineHeight': 1.8,
                #'fontSize': 18
            }

        ),
    ]
)

column2 = dbc.Col(
    [
        html.Br(),
        html.Br(),
        html.H6('Accousticness'),
        dcc.Slider(
            id='accousticness',
            min=0,
            max=100,
            step=5,
            value=50,
            marks={i:str(i) for i in range(0,100,10)},
            
        ),
        html.H6('Beats_per_minute'),
        dcc.Slider(
            id='beats_per_minute',
            min=0,
            max=250,
            step=10,
            value=125,
            marks={i:str(i) for i in range(0,250,25)},
            
        ),
        html.H6('Danceability'),
        dcc.Slider(
            id='danceability',
            min=0,
            max=100,
            step=5,
            value=50,
            marks={i:str(i) for i in range(0,100,10)},
            
        ),
        html.H6('Energy'),
        dcc.Slider(
            id='energy',
            min=0,
            max=100,
            step=5,
            value=50,
            marks={i:str(i) for i in range(0,100,10)},
            
        ),
        html.H6('Length'),
        dcc.Slider(
            id='length',
            min=100,
            max=700,
            step=50,
            value=400,
            marks={i:str(i) for i in range(100,700,100)},
            
        ),
        html.H6('Liveness'),
        dcc.Slider(
            id='liveness',
            min=0,
            max=100,
            step=5,
            value=50,
            marks={i:str(i) for i in range(0,100,10)},
            
        ),
        html.H6('Loudness(dB)'),
        dcc.Slider(
            id='loudness',
            min=-20,
            max=0,
            step=2,
            value=-10,
            marks={i:str(i) for i in range(-20,0,2)},
            
        ),
        html.H6('Speechiness'),
        dcc.Slider(
            id='speechiness',
            min=0,
            max=100,
            step=5,
            value=50,
            marks={i:str(i) for i in range(0,100,10)},
            
        ),
        html.H6('Valence'),
        dcc.Slider(
            id='valence',
            min=0,
            max=100,
            step=5,
            value=50,
            marks={i:str(i) for i in range(0,100,10)},
            
        ),
        html.H6('Year of Hit'),
        dcc.Slider(
            id='year',
            min=2010,
            max=2019,
            step=1,
            value = 2015,
            marks={i:str(i) for i in range(2010,2019,1)},
            
        ),
        html.H6('Genre'),
        dcc.Dropdown(
            id='top_genre',
            options=[
                {'label': 'pop', 'value': 'pop'},
                {'label': 'rap / r&b', 'value': 'rap / r&b'},
                {'label': 'electronic dance', 'value': 'electronic dance'},
                {'label': 'other', 'value': 'other'},              
            ],
            value='pop',
            className='mb-4',
        ),
        
        html.Br(),
        html.Br(),
    ],
    md=4,
)

column3 = dbc.Col(
    [
        html.Br(),
        html.Br(),
        dcc.Markdown('## This song will have a popularity of...',
            style={
                'textAlign': 'center',
                'fontSize': 60
            }
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(
            id='popularity',
            style={
                'textAlign': 'center',                
                'fontSize': 50,
               #'marginLeft': '20px'

            }
        ),
    ]
)

@app.callback(
    Output('popularity', 'children'),
    [Input('accousticness', 'value'),
    Input('beats_per_minute', 'value'),
    Input('danceability', 'value'),
    Input('energy', 'value'),
    Input('length', 'value'),
    Input('liveness', 'value'),
    Input('loudness', 'value'),
    Input('speechiness', 'value'),
    Input('valence', 'value'),
    Input('year', 'value'),
    Input('top_genre', 'value')]
)

def predict(accousticness, beats_per_minute, danceability, energy, length,
            liveness, loudness, speechiness, valence, year, top_genre):
    df = pd.DataFrame(
        columns = ['accousticness', 'beats_per_minute', 'danceability', 'energy', 'length',
                 'liveness', 'loudness', 'speechiness', 'valence', 'year', 'top_genre'],
        data = [[accousticness, beats_per_minute, danceability, energy, length,
            liveness, loudness, speechiness, valence, year, top_genre]]
    )
    y_pred = pipeline.predict(df)[0]
    if (y_pred > 65):
        return f'{y_pred:.0f}, likely to be a hit'
    else:
        return f'{y_pred:.0f}, likely wont top the charts'

layout = dbc.Row([column1, column2, column3])