import requests
import spotipy

from playlist_maker.models import Credential

SPOTIFY = 'Spotify'


def get_credentials():
    """
    Returns spotify credentials
    """
    return Credential.objects.filter(service=SPOTIFY)


def refresh_access_token(credentials):
    """
    Takes in spotify refresh token and returns new access token

    TODO - Better error handling
    """
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': credentials.refresh_token,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret
    }

    response = requests.post('https://accounts.spotify.com/api/token',
                             data=data)

    # If status == 200, save new access token, else throw error
    if response.status_code == requests.codes.ok:
        credentials.access_token = esponse.json()['access_token']
        credentials.full_clean()
        credentials.save()
    else:
        print response.content


def create_spotify_instance(credentials):
    """
    Returns Spotify instance using access_token

    TODO - Better error handling, maybe use logger
    """
    try:
        spotify_instance = spotipy.Spotify(auth=credentials.access_token)
        spotify_instance.current_user()
        return spotify_instance
    except spotipy.client.SpotifyException:
        print "error"


def search_track(spotify, artist, trackname):
    """
    Queries spotify for track using artist and trackname

    TODO - Add checks to match artist and trackname
    """
    query = artist + ' - ' + trackname
    result = spotify.search(query)

    if result['tracks']['total'] > 0:
        return result['tracks']['items'][0]['id']


def create_playlist(spotify, playlist_name, credentials):
    """
    Creates playlist using playlist_name as the title, returns
    id of created playlist

    TODO - Check if playlist w/ same name exists before creation
    """
    user_id = credentials.account_id
    result = spotify.user_playlist_create(user_id, playlist_name)

    return result['id']
