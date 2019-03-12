from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Design

class ABTestList(ListView):
    model = Design
    context_object_name = "abtestlist"
    template_name = "app_abtest/main/abtest_list.html"

    def get_queryset(self):
        return Design.objects.filter(is_published = True)[:5]


class ABTestDetail(DetailView):
    model = Design
    template_name = "app_abtest/main/abtest_detail.html"