import string
import random

def text_gen(size = 8, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

size        = 3
user_posts  = []
user_post   = {'title':'', 'content':'', 'slug':''}

for _ in range(size):
    user_post = {item:text_gen(random.randint(10, 15)) for item in user_post}
    user_posts.append(user_post)

for item in user_post:
	if item == 'title':
		print('title')
