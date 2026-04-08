import json
import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import OTP, User


@csrf_exempt
def send_otp(request):

    if request.method == "POST":

        data = json.loads(request.body)

        mobile = data.get("mobile")

        otp = str(random.randint(1000,9999))

        OTP.objects.create(
            mobile = mobile,
            otp = otp
        )

        print("OTP:", otp)   # temporary testing

        return JsonResponse({
    "status": True
    })
    
@csrf_exempt
def verify_otp(request):

    if request.method == "POST":

        data = json.loads(request.body)

        mobile = data.get("mobile")
        otp = data.get("otp")

        record = OTP.objects.filter(mobile=mobile, otp=otp).last()

        if record:

            request.session["mobile"] = mobile   # user logged in

            return JsonResponse({
                "status":"verified"
            })

        return JsonResponse({
            "status":"invalid"
        })
    
@csrf_exempt
def login_user(request):

    if request.method == "POST":

        data = json.loads(request.body)

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        mobile = data.get("mobile")

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "name":name,
                "password":password,
                "mobile":mobile
            }
        )

        return JsonResponse({
            "status":"success",
            "name":user.name,
            "email":user.email,
            "mobile":user.mobile
        })    
def check_login(request):

    if request.session.get("mobile"):

        return JsonResponse({
            "logged_in": True
        })

    return JsonResponse({
        "logged_in": False
    })    