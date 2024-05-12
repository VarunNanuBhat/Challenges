from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string


# Create your views here.
#def home_page(request):
 #   response_data = '''
  #      <ul>
   #         <li><a href= '/challenges/january'>January</a></li>
    #        <li><a href= '/challenges/february'>February</a></li>
     #       <li><a href= '/challenges/march'>March</a></li>
      #  </ul>
    #'''
    #return HttpResponse(response_data)

def home_page(request):
    months = ["january", "february", "march"]

    return render(request, "challenges/homepage.html", {
        "months": months
    })

'''
def monthly_challenge(request,month):
    # create a variable to store text, so that it can be updated with if else condition.
    challenge_text = None
    if month == "january":
        challenge_text = "Take a chill pill"
    #elif month == "Jan" or "jan":
        #return HttpResponseRedirect("/challenges/" + "january")
    elif month == "february":
        challenge_text = "pass internals"
    elif month == "march":
        challenge_text = "complete DBMS project"
    else:
        return HttpResponseNotFound("We are sorry, the month you entered is invalid!!!!")

    return HttpResponse(challenge_text)
'''

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Take a chill pill"
    elif month == "february":
        challenge_text = "pass internals"
    elif month == "march":
        challenge_text = "complete DBMS project"
    else:
        return HttpResponseNotFound("We are sorry, the month you entered is invalid!!!!")

    return render(request, "challenges/challenge.html", {
        "month": month,
        "text": challenge_text,
    })



