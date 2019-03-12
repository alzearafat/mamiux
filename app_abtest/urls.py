from django.contrib import admin
from django.urls import path

from . import views

app_name = 'app_abtest'
urlpatterns = [
    path('', views.ABTestList.as_view(), name = 'abtest_list'),
    path('abtest/<int:pk>', views.ABTestDetail.as_view(), name = 'abtest_detail')
]

admin.site.site_header = 'MamiUX Dashboard'
    
    # == CHEAT SHEET ==
    # path('contacts', views.ContactList.as_view(), name='contact_list'),
    # path('contact/<int:pk>', views.ContactDetail.as_view(), name='contact_detail'),
    # path('create', views.ContactCreate.as_view(), name='contact_create'),
    # path('update/<int:pk>', views.ContactUpdate.as_view(), name='contact_update'),
    # path('delete/<int:pk>', views.ContactDelete.as_view(), name='contact_delete'),