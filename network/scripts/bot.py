import requests, random, string, json
from botconf import number_of_users, max_posts_per_user, max_likes_per_user
# script instructions
# number_of_users     = botconf.number_of_users
# max_posts_per_user  = botconf.max_posts_per_user
# max_likes_per_user  = botconf.max_likes_per_user

# function generates random string
def text_gen(size=8, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

# function generates random email
def email_gen(size=8):
    return text_gen(size) + '@gmail.com'

# gets and return token depends on login info
def get_token(token_url, login_data):
	return requests.post(token_url, login_data).json()['token']

# create jwt header for token connections
def create_jwt_header(token):
	# token = get_token(token_url, login_data)
	# returns header for jwt
	return {'Authorization': f'JWT {token}'}

# create posts on scripts side
def create_posts(post, post_count=2, from_rand=10, to_rand=15):
	posts  = []
	# filling in posts data with random data(strings)
	for _ in range(post_count):
	    user_post = {item:text_gen(random.randint(from_rand, to_rand)) for item in post}
	    posts.append(user_post)
	return posts

# create posts on api side
def send_posts(posts, post_url, headers):
	for post in posts:
	    created_posts = requests.post(post_url, data = post, headers=headers).json()
	return created_posts

# create users on scripts side
def create_users(user, user_count=2, from_rand=8, to_rand=12):
	users  = []
	# filling in users data with random data(strings and email)
	for _ in range(user_count):
	    user = {item:(text_gen(random.randint(from_rand, to_rand))
				if not item == 'email' else email_gen())
				for item in user}
	    users.append(user)
	return users

# create users on api side
def send_users(users, user_url, headers):
	for user in users:
	    created_users = requests.post(user_url, data=user, headers=headers).json()
	return created_users

def send_users_and_posts(users):
	for user in users:

	    created_users = requests.post(user_url, data=user, headers=headers).json()
	return created_users

"""
	Creating multiple users&posts
"""

"""initial api urls&data templates"""
token_url   = '''http://127.0.0.1:8000/api/auth/token/'''
login_data  = {'username': 'alex', 'password': 'test1234'}

user_url    = '''http://127.0.0.1:8000/api/users/'''
user_data 	= {'username': '', 'email': '', 'password': ''}

post_url    = '''http://127.0.0.1:8000/api/posts/'''
post_data	= {'title': '', 'content': '', 'slug': ''}

token 		= get_token(token_url, login_data)
headers 	= create_jwt_header(token)
print(token)

"""create&send users&posts"""
# generates random users
users = create_users(user_data, number_of_users)
for user in users:

	# creates and authenticates users
	user_for_posts 	= {'username': f'{user["username"]}', 'password': f'{user["password"]}'}
	sended_users 	= requests.post(user_url, data=user, headers=headers).json()
	user_token 		= get_token(token_url, user_for_posts)
	jwt_header 		= create_jwt_header(user_token)

	# generates and creates random posts
	sended_posts 	= create_posts(post_data, max_posts_per_user)
	send_posts(sended_posts, post_url, jwt_header)






# def automate_creation(user_count=2, post_count=2, like_count=0):
# print(post_request.status_code, post_request.reason)
# print(post_request.text[:300] + '...')
#{'all_of_my_posts': json.dumps(user_posts)}
