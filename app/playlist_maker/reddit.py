import praw
import time
import requests

from datetime import date
from datetime import timedelta

from playlist_maker.reddit_secrets import PASSWORD
from playlist_maker.reddit_secrets import CLIENT_SECRET
from playlist_maker.reddit_secrets import CLIENT_ID


# List of supported subreddits
SUBREDDITS = ['hiphopheads']

# Disable SNIMissing Warnings, InsecurePlatformWarnings due to use older
# version of python w/ urllib3
requests.packages.urllib3.disable_warnings()


def create_reddit_instance():
    """
    Creates and returns a reddit instance w/ credentials from reddit_secrets
    script

    #TODO - check reddit instance is valid before returning
    """
    return praw.Reddit(client_id=CLIENT_ID,
                       client_secret=CLIENT_SECRET,
                       password=PASSWORD,
                       user_agent='testscript by /u/daily-reddit-playlis',
                       username='daily-reddit-playlis')


def retrieve_submissions_from_subreddit(reddit, subreddit_name):
    """
    Retrieves all submissions for a specific subreddit from previous day

    Args:
        reddit - reddit instance
        subreddit_name - name of subreddit as a string

    Returns:
        List of submissions


    # TODO - check subreddit is valid before retrieving submissions
    """
    subreddit = reddit.subreddit(subreddit_name)
    start_timestamp, end_timestamp = get_unix_timestamps_prev_day()

    submissions = subreddit.submissions(start=start_timestamp,
                                        end=end_timestamp)

    results = []
    for sub in submissions:
        results.append({
            'title': sub.title,
            'url': sub.url,
            'created': sub.created_utc
        })

    return results


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


