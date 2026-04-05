from django.contrib import admin
from django.db.models import Count
from .models import Complaint
import json


class ComplaintAdmin(admin.ModelAdmin):

    change_list_template = "admin/complaint_chart.html"

    def changelist_view(self, request, extra_context=None):

        chart_data = (
            Complaint.objects
            .values('issue_type')
            .annotate(count=Count('issue_type'))
        )

        labels = []
        data = []

        for item in chart_data:
            labels.append(item['issue_type'])
            data.append(item['count'])

        extra_context = extra_context or {}
        extra_context['labels'] = json.dumps(labels)
        extra_context['data'] = json.dumps(data)

        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Complaint, ComplaintAdmin)