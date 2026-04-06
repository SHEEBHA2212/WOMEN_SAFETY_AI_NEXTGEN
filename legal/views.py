import json
from django.http import JsonResponse
from .models import Case
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def submit_case(request):
    print("API HIT 🔥")

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("DATA RECEIVED:", data)

            case = Case.objects.create(
                name=data.get("name"),
                phone=data.get("phone"),
                issue=data.get("issue"),
                advocate=data.get("advocate")
            )

            return JsonResponse({
                "message": "Case submitted successfully ✅",
                "id": case.id
            })

        except Exception as e:
            print("ERROR:", e)
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST allowed"}, status=400)