from django.contrib import admin
from django.urls import path

from . import views

app_name = 'app_abtest'
urlpatterns = [
    path('dashboard/', views.ABTestListDashboardView, name='abtest_list_dashboard'),
    path('<int:pk>/', views.ABTestDetailTesterView, name='abtest_tester_detail'),
]

admin.site.site_header = 'MamiUX Dashboard'
