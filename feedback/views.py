import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Feedback

@csrf_exempt
@require_POST
def submit_feedback(request):
    try:
        data = json.loads(request.body)

        ratings = data.get("ratings", {})

        Feedback.objects.create(
            ease_of_use        = ratings.get("r1"),
            emergency_response = ratings.get("r2"),
            legal_assistance   = ratings.get("r3"),
            complaint_filing   = ratings.get("r4"),
            nearby_help        = ratings.get("r5"),
            overall_design     = ratings.get("r6"),

            overall_experience = data.get("overall", ""),
            recommend          = data.get("recommend", ""),
            best_feature       = data.get("bestFeature", ""),

            improvement        = data.get("improvement", ""),
            comments           = data.get("comments", ""),
            name               = data.get("name", ""),
        )

        return JsonResponse({"status": "success", "message": "Feedback saved!"})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)