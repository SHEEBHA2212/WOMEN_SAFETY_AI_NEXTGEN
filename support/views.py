from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chatbot(request):

    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "").strip().lower()

        commands = {
            "@help": "Available commands: @complaint, @status, @emergency, @contact, @feedback",
            "@complaint": "You can file a complaint here: /complaint",
            "@status": "Please enter your complaint ID to check the status.",
            "@emergency": "Emergency numbers: 100 (Police), 1091 (Women Helpline)",
            "@contact": "Municipality Helpline: 1800-123-456",
            "@feedback": "You can submit feedback on our feedback page.",
            "@report": "You can submit a report here: /report",
            "@safety": "For safety tips and resources, visit our safety page.",
            "@nearestpolice": "Find the nearest police station using our location service."
        }

        reply = commands.get(message, "Unknown command. Type @help to see available commands.")

        return JsonResponse({"reply": reply})

    return JsonResponse({"reply": "Invalid request"})