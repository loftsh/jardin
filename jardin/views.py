from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import datetime

import logging

logger = logging.getLogger(__name__)

def pumpState(request):    
    return render(request, "jardin/base.html")

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. And the pump is %s</body></html>" % (now, pump_state())
    return HttpResponse(html)

def pump_state():
    from pigpio import pi
    p = pi()
    return p.read(6)

def pump_state_view(request):
    state = pump_state()
    return JsonResponse({'state':state})

