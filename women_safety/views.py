from django.shortcuts import render
from complaint.models import Complaint
from legal.models import Case
from feedback.models import Feedback
from support.models import ContactTicket

def internal_admin_dashboard(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    cases = Case.objects.all().order_by('-id')
    feedbacks = Feedback.objects.all().order_by('-submitted_at')
    tickets = ContactTicket.objects.all().order_by('-created_at')

    context = {
        'complaints': complaints,
        'cases': cases,
        'feedbacks': feedbacks,
        'tickets': tickets
    }
    return render(request, 'admin_dashboard.html', context)
