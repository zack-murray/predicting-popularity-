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
        dcc.Markdown('## Project Insight',
        style={
                'textAlign': 'center'
                }
        ),
        html.Br(),
        html.Br(),
        dcc.Markdown(
            """
            Despite it's short-comings, this model can still provide a good deal of insight. They say that a picture is worth a thousand words, so let's analyze some of these visualizations to get a better break down of our model. 
            
            The first visualization that we'd like to draw your attention to is our models permuation importances. These importances are alotted by checking the evaluation metric, in our case R^2, and seeing how the score decreases when select features aren't made available. This is very important process in the making of the model, as it allows us to narrow down features in an attempt to improve our score and combat overfitting. 
            """
         ),
        html.Br(),
        html.Div(
            html.Img(src='assets/permimportances.png', className='img-fluid', width=300), 
            style={'textAlign': 'center'}
        ),
        html.Br(),
        dcc.Markdown(
            """
            According to our permutation importances, the most important feature is 'year' and works its way down the list until it gets to it's least important feature, top_genre_2. Those numbers displayed under weight look super confusing, but looks can be deceiving. If you look at the 'year' feature, the weight next to it shows 0.2639 +/- 0.0464. Basically all this weight is saying, is that if you re-arranged all of the values in that feature while keeping all other features the same, that the prediction will be changed on average .2639 +/- .0464 popularity. It's worth noting here that year is included in the diagnosis because we opted against a time-series split. With a random train / test split, the year feature will not bias the data like a time based split would, and instead provides the most value to our model. Another noteworthy observation is the impact of energy. Energy is surprisingly about half way down the feature importance list, amazing considering its seeming close correlation to danceability. But, as stated above, looks can be deceiving. Let's take a look at this pdp plot comparing the two. 
            """
        ),
        html.Div(
            html.Img(src='assets/energydanceability.png', className='img-fluid', width=500), 
            style={'textAlign': 'center'}
        ),
        html.Br(),
        dcc.Markdown(
            """
            When visualizing this plot, it's worth understanding that the lighter the color (and higher the number inside), the better the two correlate in providing a higher song popularity. When creating this model, I hypothesized that a high energy would correspond with high danceability and in return, predict high popularity. But when looking at the plot, it seems that the best indicator for a hit takes into account just about a medium to high danceability, while maintaing a relatively low energy, roughly any value under 70. Too much energy in a song is detrimental to it's popularity, any interesting perspective to keep with you as you explore new music in hopes of a hit.

            Length was another interesting feature. In this model, length is a metric that divulges song time from start to finish (in seconds), and is our 4th highest permuated importance. Until the final model was attempted, almost every exploratory model had length being the top importance. Before diving into this, let's take a look at it's pdp plot.
            """
        ),
        html.Div(
            html.Img(src='assets/length.png', className='img-fluid',width=800), 
            style={'textAlign': 'center'}
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        dcc.Markdown(
            """
            What an interesting result. First, the song with the shortest duration in this dataset is 134 seconds long, or 2 minutes and 14 seconds. The plot shows there being a slight negative association with short songs, which is exactly what you might expect. Short songs leave people wanting more, especially if they're catchy, which can leave a bad taste in the listener's ear (mouth, sorry can't help it). However, this plot still displays the right context, as popularity continues to rise until a certain point and then dips off. This goes in line exactly with our thinking, as long songs share similar short-comings to their minimally timed counterparts. Even a really good song can be found repetitive and dull if taken past a certain point. This plot illustrates that there's a sweet spot when trying to conceive a hit song, from about 180 seconds all the way to about 300 secounds, where popularity starts to fall off promptly.

            The last visualization that I wan't to draw your attention to is this shapley plot.
            """
        ),
        html.Br(),
        html.Br(),
        html.Div(
            html.Img(src='assets/shapplot1.png', className='img-fluid',width=1200), 
            style={'textAlign': 'center'}
        ),
        html.Br(),
        html.Br(),
        dcc.Markdown(
            """
            Shapley plots are another useful way to understand feature importances. For this example, we picked one song from the dataset and plotted it to analyze each metrics significance. There's two big takeaways from this style of graph, color and length. Features in blue have a positive impact on the popularity prediction, while red features impact the model negatively. With that in mind, the longer the bar of a feature, the greater its importance to that popularity rating. So with this example song, can you guess what the biggest positive influential feature is? If you said, 'year = 2014', you're correct! With this is mind, you can see how popular these plots can be because of their readability and ease of understanding. However, not all shapley plots are equal, as some are not so easily understood. Take this shapley plot for example.  
            """
        ),
        html.Br(),
        html.Br(),
        html.Div(
            html.Img(src='assets/shapplot2.png', className='img-fluid', width=1000), 
            style={'textAlign': 'center'}
        ),
        html.Br(),
        html.Br(),
        dcc.Markdown(
            """
            Despite it's cool design, from first glance you probably have some hestitation as to what this graph is trying display to you. And that's because instead of the plot applying the features to one song, it's applying them across the entire dataset. When working this this plot in our notebooks, we can hover along the visualization to see what's beneficial on the left (for high popularity songs) and what's diminishing that popularity as we head to the right. The sheer amount of lines introduces a lot of 'noise' to the plot, but with careful insight and investigation, it can also provide to be a very useful tool. 
            """
        ),
    ],
)

layout = dbc.Row([column1])