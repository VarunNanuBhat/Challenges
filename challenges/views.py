from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.


#def monthly_challenge_url_redirect (request, month):


def monthly_challenge (request, month):
    # create a variable to store text, so that it can be updated with if else condition.
    challenge_text = None
    if month == "january":
        challenge_text = "Take a chill pill"
    elif month == "Jan" or "jan":
        return HttpResponseRedirect("/challenges/" + "january")
    elif month == "february":
        challenge_text = "pass internals"
    elif month == "march":
        challenge_text = "complete DBMS project"
    else:
        return HttpResponseNotFound("We are sorry, the month you entered is invalid!!!!")

    return HttpResponse(challenge_text)