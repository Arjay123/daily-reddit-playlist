import praw
from datetime import date
from datetime import timedelta

yesterday = date.today() - timedelta(1)
reddit = praw.Reddit(client_id='fplo6x7x8_Q10Q',
                     client_secret='yrB5IRgYtN5d1Xky2zmhOUKhWsU',
                     password='8899009988@#$',
                     user_agent='testscript by /u/daily-reddit-playlis',
                     username='daily-reddit-playlis')

# UNIX Timestamp
time.mktime(yesterday.timetuple())