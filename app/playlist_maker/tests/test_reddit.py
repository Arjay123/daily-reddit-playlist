from django.test import TestCase
from playlist_maker.reddit import get_unix_timestamps_prev_day

from datetime import datetime
from datetime import timedelta

class RedditTestCase(TestCase):
    def test_get_unix_timestamps_prev_day(self):

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
