import requests
import spotipy

def refresh_access_token(refresh_token, client_id, client_secret):
    """
    Takes in spotify refresh token and returns new access token

    TODO - Better error handling
    """
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post('https://accounts.spotify.com/api/token',
                             data=data)

    # If status == 200, return access token, else throw error
    if response.status_code == requests.codes.ok:
        return response.json()['access_token']
    else:
        print response.content


def create_spotify_instance(access_token):
    """
    Returns Spotify instance using access_token

    TODO - Better error handling, maybe use logger
    """
    try:
        spotify_instance = spotipy.Spotify(auth=access_token)
        spotify_instance.current_user()
        return spotify_instance
    except spotipy.client.SpotifyException:
        print "error"


def search_track(spotify, artist, trackname):
    """
    """
    query = artist + ' - ' + trackname
    result = spotify.search(query)

    if result['tracks']['total'] > 0:
        # TODO - Add checks to match artist and trackname
        return result['tracks']['items'][0]['id']
