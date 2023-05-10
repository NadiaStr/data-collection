import praw
import pandas as pd
import csv
import datetime
import pprint

reddit = praw.Reddit(client_id='rb8Hwu7-UIpDKA',
                     client_secret='m8bywptTerUtYpjZU10NSKNU8jY',
                     user_agent='for Reddit WebScrapping')

#get 3 top posts from the ConfidentlyIncorrect subreddit
top_posts = reddit.subreddit('ConfidentlyIncorrect').top(limit=3)
for post in top_posts:
    print(post.title)

subs = []
subCount = 0
sub_entries = {}

posts = []
vc_subreddit = reddit.subreddit('ConfidentlyIncorrect')
for post in vc_subreddit.top(time_filter='year', limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, datetime.datetime.fromtimestamp(post.created)])
posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)
posts.to_excel('.../vaccinesyear.xlsx')

query = ['RedditData']

for item in query:
    comments_dict = {
        'comment_id': [],  # unique comm id
        'comment_parent_id': [],  # comment parent id
        'comment_link_id': [],  # link to the comment
        'comment_replies': [],  # instanceof comment forrest
        'comment_created': [],  # date of the comment
        'comment_author': [],  # author of the comment
        'comment_body': [],  # comment text
        'comment_score': [],  # comment text
        'comment_distinguished': [],  # whether comment is distinguished
        'comment_stickied': []  # whether comment is stickied
    }

submission = reddit.submission(url="https://www.reddit.com/r/conspiracy/comments/jt6sxg/say_no_to_using_the_us_military_as_guinea_pigs/")
submission.comment_sort = 'new'
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    comments_dict['comment_id'].append(comment.id)
    comments_dict['comment_parent_id'].append(comment.parent_id)
    comments_dict['comment_link_id'].append(comment.link_id)
    comments_dict['comment_replies'].append(comment.replies)
    comments_dict['comment_created'].append(datetime.datetime.fromtimestamp(comment.created))
    comments_dict['comment_author'].append(comment.author)
    comments_dict['comment_body'].append(comment.body)
    comments_dict['comment_score'].append(comment.score)
    comments_dict['comment_distinguished'].append(comment.distinguished)
    comments_dict['comment_stickied'].append(comment.stickied)
                
comments = pd.DataFrame(comments_dict,columns=['comment_id','comment_parent_id','comment_link_id','comment_replies', 'comment_created', 'comment_author', 'comment_body', 'comment_score','comment_distinguished', 'comment_stickied'])
print(comments)
pd.DataFrame(comments,columns=['comment_id','comment_parent_id','comment_link_id','comment_replies', 'comment_created', 'comment_author', 'comment_body', 'comment_score','comment_distinguished', 'comment_stickied']).to_excel('.../jt6sxg.xlsx')

print('')
print('XXXXXX')
print('')




