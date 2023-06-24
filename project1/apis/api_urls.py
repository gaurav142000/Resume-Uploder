from django.urls import path
from apis.views import ResumeView

urlpatterns = [
    path('Resume_api/',ResumeView.as_view()),
]
