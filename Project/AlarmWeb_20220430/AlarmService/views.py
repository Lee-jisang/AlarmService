from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from AlarmService.models import *

from AlarmService.sleep import Blink_Detector

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder

from django.utils import timezone
from datetime import datetime

import json

#import TaskManager.consumers

# Create your views here.
def main(req):
    context = {

    }
    return render(req, "main.html", context=context)

def Alarm(req):
    context = {

    }
    return render(req, "Alarm.html", context=context)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def blink_detector(request):
    return StreamingHttpResponse(gen(Blink_Detector()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')