import praw

r = praw.Reddit(user_agent='Karma breakdown 1.0 by /u/danielvd')
print "Enter the username"
user_name = str(raw_input())
user_name = user_name.rstrip()
user = r.get_redditor(user_name)
thing_limit = 10 
gen = user.get_submitted(limit=thing_limit)
karma_by_subreddit = {}

for thing in gen: 
	subreddit = thing.subreddit.display_name
	karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit,0) + thing.score)
	print subreddit, thing.score


