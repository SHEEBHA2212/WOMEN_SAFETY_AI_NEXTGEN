from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Evidence

@api_view(['POST'])
def upload_video(request):
    file = request.FILES.get('video')

    if file:
        evidence = Evidence.objects.create(video=file)
        return Response({"message": "Saved", "id": evidence.id})

    return Response({"error": "No file"}, status=400)