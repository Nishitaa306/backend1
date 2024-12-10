from django.urls import path
from dashboard import views
from .views import RegisterUserView, LoginUserView, ReportListCreateView, ReportDetailView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('reports/', ReportListCreateView.as_view(), name='reports'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
]
