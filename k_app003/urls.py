from django.urls import path
from . import views

app_name = 'k_app003'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('k_app003-list/', views.DiaryListView.as_view(), name="k_app003_list")


]