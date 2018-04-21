#!/usr/bin/python3


import praw

name = 'personal_app'
api = 'SxPoFInjKOTUGWBQAf_A5i8hYjg'

reddit = praw.Reddit(client_id=name, client_secret=api, user_agent='personal non commercial reddit')


#for submission in reddit.subreddit('schizophrenia').new(limit=10):
#    print(submission.title)
    
