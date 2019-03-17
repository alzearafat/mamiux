from django.contrib import admin
from django.urls import path

from . import views

app_name = 'app_abtest'
urlpatterns = [

    # DASHBOARD
    path('dashboard/', views.ABTestListDashboardView, name='abtest_list_dashboard'),
    path('dashboard/test/<int:pk>/', views.ABTestDetailDashboardView, name='abtest_results'),

    # TESTER
    path('<int:pk>/', views.ABTestDetailTesterView, name='abtest_tester_detail'),
    path('maacih/', views.ABTestThanksView, name='abtest_thanks'),
    
]

admin.site.site_header = 'MamiUX Dashboard'
