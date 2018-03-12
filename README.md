# social-network
Social Network: Rest Full API

~Default Urls~

-user urls
http://127.0.0.1:8000/users/signup/
http://127.0.0.1:8000/users/login/
http://127.0.0.1:8000/users/profile/
http://127.0.0.1:8000/users/profile/edit
-post urls
http://127.0.0.1:8000/posts/
http://127.0.0.1:8000/posts/create
http://127.0.0.1:8000/posts/<title>
http://127.0.0.1:8000/posts/<title>/edit

~Default API Urls~

-token url
'''http://127.0.0.1:8000/api/auth/token/'''
login_data  = {'username': 'alex', 'password': 'test1234'}

-users url
'''http://127.0.0.1:8000/api/users/'''
-example of user sign-up data
{'username': '', 'email': '', 'password': ''}

-posts url
'''http://127.0.0.1:8000/api/posts/'''
-example of post-create data
{'title': '', 'content': '', 'slug': ''}


***ADD-FIX***
-edit posts permission only for authorized users
-add likes to posts, to bot randomizer
-write tests
-write user&post manager
-use viewset for multiple serializers instead of generic
-replace the rest of function views by class(generic) views
-look up rest-auth for user api replacement
