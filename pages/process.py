# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown("## The Process",
            style={
                'textAlign': 'center'
                }
        ),
        html.Br(),
        html.Br(),
        dcc.Markdown(
            """
            No matter the reason, music is an intricate part of most people's lives, whether it be performing or listening. Music can be a useful tool to express our feeling and convey our emotions to one another. Take a minute to reflect on how often we appreciate music without cognizantly thinking about it. When you're commuting to or from work, usually there is music playing. Out to eat at a restaurant, taking the elevator, spending time with family and friends at a gathering? More often than not music is present, because even as just background noise, we derive joy from the beautiful sounds that fill an otherwise  dull and dreary silence.

            While music taste is subjective, a certain sound captivates wide audiences, and that sound is often looked to or replicated in an effort to produce music with the widest appeal. Billboard magazine, in particulur, recognizes these popularized sounds/songs and broadcasts them in a 'Top Chart' published at the end of every year. A Spotify playlist containing roughly the top 60 songs from every year this decade was created and put through Spotify's, "Ogranize your music", app. This app, official from Spotify, scans through given playlists and assigns performance attributes to each song. I pulled this data to see if there was a correlation in the combination of those attributes to song popularity.

            The evaluation attributes that spotify provides through their app are accousticness, beats_per_minute, danceability, energy, length, liveness, loudness(dB), popularity, and speechiness.  Given these variables, it was easy to pick 'popularity' as the target for my prediction. Since the popularity variable is output as a continuous variable, we decided to approach this as a regression problem. By taking the mean, or average, of the popularity column, we establish our baseline. Our baseline is  a beginner model to which we will  build on to improve effectiveness. We baseline derived a popularity of 68% and an MAE, or mean-absolute error, of 9.56. This means if we just guessed every song had a popularity of 68%, we would be off by 9.56 on average. Later models will be evaluated using the R^2 and MAE metrics, but because the baseline R^2 is always zero, we've decided to digress.

            A random test / train split was utilized for this model, despite a time-based split being more ideal. The reason behind this is the popularity attribute itself, as 2019's song popularity was greatly skewed right (had significantly higher popularity on average). When applying the test set, the information we want to predict, to 2019, we were unable to succesfully reproduce a positive R^2 value meaning that our model was no better than the baseline. You can see the discretion of popularity in the image below.
            
            """,
            #style={'fontFamily':'Verdana', 'fontWeight': 'normal', 'fontSize': 'smaller'}
        ),
        html.Div(
            html.Img(src='assets/songpopbyyear.png', className='img-fluid', width=500), 
            style={'textAlign': 'center'}
        ),
        dcc.Markdown(

            """
            After splitting the data, we tried to improve on our base model by fitting a linear regression model. The results were unimpressive, though we do see a minor improvement in the training set comapared to the baseline. 
            * Linear Regression train R^2: 0.1313,  or 13.13%
            * Linear Regression train MAE: 8.50 popularity
            * Linear Regression test R^2: -0.0172 or - 1.72% 
            * Linear Regression test MAE: 10.62 popularity

            The results of the linear regression were demoralizing, but we pressed on. We decided to try a tree-based model, more specifically, a Random Forest Regressor. Cross validation was applied to this model in an attempt to prevent overfitting, as well as tuning the models hyperparameters to their optimal settings. Despite not setting the world on fire, increasingly improved test results were achieved. 
            * Random Forest Regression test R^2: 0.1347, or 13% (huge, up from a negative R^2)
            * Random Forest Regression test MAE: 8.59 popularity

            Now, don't get us wrong, this model isn't perfect. Basically what these results are stating is that this Random Forest Regressor can account for roughly 14% of new data with an average error of 8.56 popularity. Ideally our model would be able to predict a far higher percent of new data and with less average error, but given the relatively small size of the dataset and our unfavorable linear regression model, we're proud of the results we achieved. In the future, it would be interesting to see this project reproduced with increased observations and more descriptive analytics.

            """,
            #style={'fontFamily':'Verdana', 'fontWeight': 'normal', 'fontSize': 'smaller'}
        ),

    ],
)

layout = dbc.Row([column1])