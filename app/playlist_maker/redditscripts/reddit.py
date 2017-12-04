import praw
from datetime import date
from datetime import timedelta

from reddit_secrets import PASSWORD
from reddit_secrets import CLIENT_SECRET
from reddit_secrets import CLIENT_ID


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
    # yesterday = date.today() - timedelta(1)

    # # UNIX Timestamp
    # time.mktime(yesterday.timetuple())
    pass


def filter_song_and_artist(sub_title):
    """
    Checks a submission title against a regex and returns a tuple in the form
    of (artist, trackname) if the submission is a song submission
    """
    pass


