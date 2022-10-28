from django.http import HttpResponse
import json

# Create your views here.

# HomePage
def home(request):

    responseData = {
        "slackUsername": "elemasamuel",
        "backend": True,
        "age": 21,
        "bio": "I'm a Backend Developer, specializing in Python.",
    }

    return HttpResponse(json.dumps(responseData), content_type="application/json")
