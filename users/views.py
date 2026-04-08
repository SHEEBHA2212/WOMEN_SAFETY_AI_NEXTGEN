from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

@csrf_exempt
def save_user(request):
    if request.method == "POST":
        data = json.loads(request.body)

        name = data.get("name")
        mobile = data.get("mobile")

        try:
            user = User.objects.get(name=name, mobile=mobile)
            return JsonResponse({"status": "success"})
        except User.DoesNotExist:
            return JsonResponse({"status": "failed"})