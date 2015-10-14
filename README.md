# django rest api example!

This is a very brief and readable REST API written in python and backed by django.
          
Plain, vanilla django. no modules or extra packages needed. NOT DJANGO REST FRAMEWORK!

You can run it as is by using manage.py runserver, and doing a GET to "localhost:portnumber"
for example, GET to localhost:8080/users/123/ to get a dictionary like:
   {"name" "bob", "mail": "mackieb@email.com", "blurb": "Wow, Bob Mackie!"}

There is only one model this API can create/edit/delete/get: RestUser in the 'main' django app.

  To create a user, send a POST with a json payload to /users/ in this format:
      
      {"name": "some_string", "mail": "valid_email", "blurb": "some_string"}
      
  To edit user_id 123's fields, send a PUT with a json payload to /users/123 in this format:
      
      {"name": "some_new_string", "mail": "new_valid_email", "blurb": "some_new_string"}
      
  To delete a user with user_id 123, send an http DELETE to /users/123

Questions, criticism always welcome: turner.micah@gmail.com
