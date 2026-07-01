from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingView.as_view(), name='landing'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('download/handbook/', views.DownloadHandbookView.as_view(), name='download_handbook'),
     path(
        "dev/backup/flag-4d9b2e/",
        views.internal_backup,
        name="internal_backup",
    ),
]
