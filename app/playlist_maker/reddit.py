import praw
import time
from datetime import date
from datetime import timedelta

from playlist_maker.reddit_secrets import PASSWORD
from playlist_maker.reddit_secrets import CLIENT_SECRET
from playlist_maker.reddit_secrets import CLIENT_ID


SUBREDDITS = ['hiphopheads']

def create_reddit_instance():
    """
    Creates and returns a reddit instance w/ credentials from reddit_secrets
    script
    """
    return praw.Reddit(client_id=CLIENT_ID,
                       client_secret=CLIENT_SECRET,
                       password=PASSWORD,
                       user_agent='testscript by /u/daily-reddit-playlis',
                       username='daily-reddit-playlis')


def retrieve_submissions_from_subreddit(reddit, subreddit):
    """
    Retrieves all submissions for a specific subreddit from previous day

    Args:
        reddit - reddit instance
        subreddit - title of subreddit as a string

    Returns:
        List of submissions
    """
    pass


def get_unix_timestamps_prev_day():
    """
    Returns start and end UNIX timestamps for the previous day
    """
    today = date.today()
    yesterday = today + timedelta(days=-1)

    yesterday_start_timestamp = time.mktime(yesterday.timetuple())
    yesterday_end_timestamp = time.mktime(today.timetuple()) - 1

    return yesterday_start_timestamp, yesterday_end_timestamp


def filter_song_and_artist(sub_title):
    """
    Checks a submission title against a regex and returns a tuple in the form
    of (artist, trackname) if the submission is a song submission
    """
    pass


