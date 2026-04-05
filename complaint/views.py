from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Complaint
import json


# CREATE COMPLAINT
@csrf_exempt
def create_complaint(request):
    if request.method == "POST":
        data = json.loads(request.body)

        complaint = Complaint.objects.create(
            issue_type=data.get("issue_type"),
            location=data.get("location"),
            description=data.get("description"),
            contact=data.get("contact")
        )

        return JsonResponse({
            "message": "Complaint submitted successfully",
            "id": complaint.id
        })


# READ ALL COMPLAINTS
def get_complaints(request):

    complaints = list(Complaint.objects.values())

    return JsonResponse({
        "complaints": complaints
    })


# DELETE COMPLAINT
@csrf_exempt
def delete_complaint(request, complaint_id):

    Complaint.objects.filter(id=complaint_id).delete()

    return JsonResponse({
        "message": "Complaint deleted"
    })