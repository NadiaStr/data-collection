
import praw
import datetime

# Set up the Reddit instance
r = praw.Reddit(
    client_id='rb8Hwu7-UIpDKA',
    client_secret='m8bywptTerUtYpjZU10NSKNU8jY',
    user_agent='for Reddit WebScrapping'
)

# Set up the subreddit instance
subreddit = r.subreddit('Vaccines')

# Initialize variables
subs = []
subCount = 0
sub_entries = {}

# Search for submissions
for submission in subreddit.search('vaccines', sort='top', time_filter='week', limit=None):
    subs.append(submission.id)
    subCount += 1

# Print the results
print(str(subCount) + " submissions have been added to the list")
print("1st entry is:")
print(r.submission(id=str(subs[0])).title + " Created on: " + str(datetime.datetime.fromtimestamp(r.submission(id=str(subs[0])).created)))
print("Last entry is:")
print(r.submission(id=str(subs[subCount-1])).title + " Created on: " + str(datetime.datetime.fromtimestamp(r.submission(id=str(subs[subCount-1])).created)))