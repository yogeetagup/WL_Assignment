import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from django.db.models import Count
from .models import Account


def accountlist(request):
    return HttpResponse("wowlabs")


def usersList(request):
    data = list(User.objects.values())
    return JsonResponse(data, safe=False)


def signedUser(request):
    data = list(Account.objects.values("user_id").annotate(total=Count('id')))
    return JsonResponse(data, safe=False)


@require_http_methods(["POST"])
def loginrequest(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    username = body["username"]
    password = body["password"]
    print("username ", username)
    print("password ", password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        account_record = Account(user=user)
        account_record.save()
        return HttpResponse("login Successful")
    else:
        user = User.objects.create_user(username, "", password)
        user.save()
        return HttpResponse("User Created")
