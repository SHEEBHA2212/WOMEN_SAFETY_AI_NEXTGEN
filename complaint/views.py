from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Complaint
import json


# CREATE COMPLAINT
@csrf_exempt
def create_complaint(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            complaint = Complaint.objects.create(
                issue_type=data.get("issue_type"),
                location=data.get("location"),
                description=data.get("description"),
                contact=data.get("contact")
            )

            return JsonResponse({
                "message": "Complaint submitted successfully",
                "complaint_id": complaint.complaint_id,
                "status": complaint.status
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=405)

# READ ALL COMPLAINTS
def get_complaints(request):

    complaints = list(Complaint.objects.values())

    return JsonResponse({
        "complaints": complaints
    })


# DELETE COMPLAINT
@csrf_exempt
def delete_complaint(request, complaint_id):
    Complaint.objects.filter(complaint_id=complaint_id).delete()  # ✅ FIXED

    return JsonResponse({
        "message": "Complaint deleted"
    })

# TRACK COMPLAINT BY ID
def track_complaint(request, complaint_id):
    try:
        complaint = Complaint.objects.get(complaint_id=complaint_id)  # ✅ FIXED

        return JsonResponse({
            "complaint_id": complaint.complaint_id,
            "status": complaint.status,
            "issue_type": complaint.issue_type,
            "created_at": complaint.created_at
        })

    except Complaint.DoesNotExist:
        return JsonResponse({"error": "Complaint not found"}, status=404)
