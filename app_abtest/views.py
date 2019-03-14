from datetime import datetime
from django.utils import timezone
from app_user.models import Tester
from .forms import ABTestCommentModelForm
from .models import Design, DesignComment
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# DASHBOARD VIEWS -----------------

@login_required
def ABTestListDashboardView(request):

    """
    Render All A/B Test List
    :param request:
    :return:
    """

    # Make sure only staff can access this page
    if not request.user.is_staff:
        raise PermissionDenied
    else:
        abtest_list_dashboard = Design.objects.filter(is_published = True).order_by("-is_created")
        template = "app_abtest/dashboard/abtest_dashboard_list.html"
        paginator = Paginator(abtest_list_dashboard, 10)
        page = request.GET.get('page', 1)
        try:
            abtest_list_dashboard = paginator.page(page)
        except PageNotAnInteger:
            abtest_list_dashboard = paginator.page(1)
        except EmptyPage:
            abtest_list_dashboard = paginator.page(paginator.num_pages)
        context = {'abtest_list_dashboard': abtest_list_dashboard}
        return render(request, template, context)

# ---------------------------


# TESTER VIEWS -----------------

@login_required
def ABTestDetailTesterView(request, pk):

    """
    Render Single Thread, Comments and Comment Form
    :param request:
    :param pk:
    :return:
    """

    try:
        abtest = Design.objects.get(pk=pk)
    except Design.DoesNotExist:
        return request('/') #Nanti harus ke 404

    form = ABTestCommentModelForm()
    template = "app_abtest/tester/abtest_tester_detail.html"
    context = {'abtest': abtest, 'form': form}
    if request.method == "POST":
        form = ABTestCommentModelForm(request.POST)
        if form.is_valid():
            result = form.save(commit = False)
            result.design_abtest_title = Design.objects.get(design_title=abtest.design_title)
            result.design_abtest_tester_user = Tester.objects.get(user=request.user)
            result.is_created = datetime.now()
            result.abtest = abtest
            result.save()
            return redirect("/") #Nanti harus thank you page
    else:
        return render(request, template, context)


# ---------------------------