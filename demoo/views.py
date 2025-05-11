from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sympy.strategies.core import switch
from django.http import HttpResponse


# restful, use request.method to specify operations
@csrf_exempt    # to solve post 403: CSRF verification failed. Request aborted
def splurge(request):
    rsp = ""
    match request.method:
        case "GET":
            rsp = {"imperative": "it is absolutely imperative that we finish by this week, moral imperative",
                   "notleast": "last but not least"}
        case "POST":  # add
            rsp = {"indolent": "lazy, indolent person"}

        case "PUT":  # update
            rsp = {"warm": "i'm starting to warm to this idea now"}

        case "DELETE":
            rsp = {"coincide": "interests don't always coincide, trips don't coincide"}

    return HttpResponse(str(rsp))
