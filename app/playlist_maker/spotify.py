import requests


def refresh_access_token(refresh_token, client_id, client_secret):
    """
    Takes in spotify refresh token and returns new access token
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
        # TODO - Better error handling
        print response.content