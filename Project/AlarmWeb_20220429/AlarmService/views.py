from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from AlarmService.models import *

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