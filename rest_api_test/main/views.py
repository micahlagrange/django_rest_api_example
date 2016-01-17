"""
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

    Questions, criticism welcome: turner.micah@gmail.com
"""

# Default library
import json
import random

# Django library
from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# ## Not using csrf tokens because this is a RESTful API, not a webpage.
from django.views.decorators.csrf import csrf_exempt

# API functions
from main.models import RestUser


def decode_request(req):
    try:
        return json.loads(req.body.decode('utf-8'))
    except Exception:
        return json.loads(req.body)

@csrf_exempt
def make_user(request):
    if request.method == 'PUT':
        payload = decode_request(request)

        u = RestUser()
        u.name = payload['name']
        u.mail = payload['mail']
        u.blurb = payload['blurb']
        u.save()

        return JsonResponse(data=model_to_dict(u), status=201)
    else:
        return JsonResponse(data={"error": "incorrect HTTP method used"}, status=403)


@csrf_exempt
def user_by_id(request, user_id):
    if request.method == 'GET':
        u = get_object_or_404(RestUser, pk=user_id)
        res = dict(
            user_id=u.pk,
            name=u.name,
            mail=u.mail,
            blub=u.blurb,
        )
        return JsonResponse(res, status=200)

    elif request.method == 'POST':
        payload = decode_request(request)

        try:
            u.name = payload['name']
            u.mail = payload['mail']
            u.blurb = payload['blurb']
            u.full_clean()
            u.save()
        except ValidationError as e:
            err = []
            for field, errors in e.message_dict.items():
                err.append({"fieldName": field, "errors": ", ".join(errors)})

            errors_dict = {"error": "validation failed", "field errors": err}
            return JsonResponse(status=400, data=errors_dict)

        return JsonResponse(status=204, data={})

    elif request.method == 'DELETE':
        u = get_object_or_404(RestUser, pk=user_id)

        if 'DISABLED_' not in u.mail and 'DISABLED_' not in u.name:
            rand_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

            new_name = 'DISABLED_{}_{}'.format(''.join(random.choice(rand_str) for _ in range(8)), u.name)
            new_mail = 'DISABLED_{}_{}'.format(''.join(random.choice(rand_str) for _ in range(8)), u.mail)

            u.name = new_name
            u.mail = new_mail
            u.save()

            return JsonResponse(status=204, data={})

        else:
            return JsonResponse(status=404, data={"message": "User already deleted"})

    else:
        return JsonResponse(data={"message": "Invalid http method {}".format(request.method)},
                            status=400)
