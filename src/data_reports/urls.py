from django.urls import path
from .views import (
    create_report,
    ReportListView,
    ReportDetailView,
    UploadTemplateView,
    render_pdf_view,
    csv_upload
)

app_name = 'data_reports'

urlpatterns = [
    path('', ReportListView.as_view(), name='main'),
    path('save/', create_report, name='create_report'),
    path('upload/', csv_upload, name='upload'),
    path('from_file/', UploadTemplateView.as_view(), name='from_file'),
    path('<pk>/', ReportDetailView.as_view(), name='detail'),
    path('<pk>/pdf/', render_pdf_view, name='pdf'),
]
