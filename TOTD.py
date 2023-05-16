""" Introduction:
Course: CST 205 Section 1 - Multimedia Design & Programming

Title: TOTD (TRENDS OF THE DAY)

Abstract: This is a flask app to show daily trends of the top 
platforms on the internet to enhance marketing.

Authors: Aaron Johnson, Eunice Sosa, Sebastian Ramos, Mikaela Lagumbay

Date: May 18, 2023

Work by Aaron Johnson:
1. Researched and found Trend info for several platforms
2. Created the flask app
3. Created the basic structure of the index.html file
4. Used some boostrap to make the website look better

Work by Eunice Sosa:
1. Researched and found Trend info for several platforms

Work by Sebastian Ramos:
1. Researched and found Trend info for several platforms

Work by Mikaela Lagumbay:
1. Researched and found Trend info for several platforms

"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import requests
from PIL import Image

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# API Section

# SPOTIFY
ssl._create_default_https_context = ssl._create_unverified_context
spotify_daily_site = 'https://kworb.net/spotify/country/us_daily.html'
spotify_daily_soup = BeautifulSoup(urlopen(spotify_daily_site).read(), 'html.parser')
spotify_top = spotify_daily_soup.find('td',{'class':'text mp'}).get_text().split('-')
spotify_artist_site = 'https://kworb.net/spotify/artists.html'
spotify_top_soup = BeautifulSoup(urlopen(spotify_artist_site).read(), 'html.parser')
top_artist = spotify_top_soup.find_all('td')[0].get_text()
spotify_song_site = 'https://kworb.net/spotify/toplists.html'
spotify_song_soup = BeautifulSoup(urlopen(spotify_song_site).read(), 'html.parser')
top_song = spotify_song_soup.find_all('td')[1].get_text().split('-')
spotify_info = {
    'song' : spotify_top[1],
    'artist' : spotify_top[0],
    'top_artist' : top_artist,
    'top_song_title' : top_song[1],
    'top_song_artist' : top_song[0]
}
# END SPOTIFY

#END API Section

@app.route('/')
def home():
    return render_template('index.html', spotify=spotify_top[0])

@app.route('/spotifyTrends')
def spotifyTrends():
    return render_template('spotifyTrends.html', spotify=spotify_info)