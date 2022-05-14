from AlarmService.models import *
from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
import AlarmService.sleep

def main(req):
    context = {

    }
    return render(req, "main.html", context=context)

def Alarm(req):
    context = {

    }
    return render(req, "Alarm.html", context=context)

def StopAlarm(req):
    context = {

    }
    return render(req, "StopAlarm.html", context=context)




@csrf_exempt
def ajax_connect_config(request):
    receive_message = request.POST.get('send_data')
    print(AlarmService.sleep.check)
    if AlarmService.sleep.check == True:
        send_message = {'send_data': '0'}
    else:
        send_message = {'send_data': '1'}
    return JsonResponse(send_message)





def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def blink_detector(request):
    return StreamingHttpResponse(gen(AlarmService.sleep.Blink_Detector()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')