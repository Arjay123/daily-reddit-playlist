from django.test import TestCase
from playlist_maker.reddit import get_unix_timestamps_prev_day
from playlist_maker.reddit import retrieve_submissions_from_subreddit
from playlist_maker.reddit import create_reddit_instance

from datetime import datetime
from datetime import timedelta

class RedditTestCase(TestCase):
    def test_get_unix_timestamps_prev_day(self):
        """
        Test that unix timestamps are for start and end of previous day
        """
        today = datetime.today()
        yesterday = today - timedelta(1)

        expected_start = datetime(year=yesterday.year,
                                   month=yesterday.month,
                                   day=yesterday.day)

        expected_end = expected_start.replace(hour=23,
                                                minute=59,
                                                second=59)

        yesterday_start_ts, yesterday_end_ts = get_unix_timestamps_prev_day()
        yesterday_start = datetime.fromtimestamp(yesterday_start_ts)
        yesterday_end = datetime.fromtimestamp(yesterday_end_ts)

        self.assertEquals(expected_start, yesterday_start)
        self.assertEquals(expected_end, yesterday_end)


    def test_retrieve_submissions_from_subreddit_returns_valid_subs(self):
        start, end = get_unix_timestamps_prev_day()

        reddit = create_reddit_instance()
        submissions = retrieve_submissions_from_subreddit(reddit, 'hiphopheads')

        for sub in submissions:
            self.assertEquals(True, sub['created'] >= start)
            self.assertEquals(True, sub['created'] <= end)
