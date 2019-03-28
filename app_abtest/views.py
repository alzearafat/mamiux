from datetime import datetime
from app_user.models import Tester
from django.db.models import Count
from django.http import HttpResponseRedirect
from .forms import ABTestCommentModelForm
from .models import Design, DesignComment
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# STATIC PAGE VIEWS -----------------

def ABTestStaticHomepageView(request):

    """
    Render Homepage Static
    :param request:
    :return:
    """

    template = "app_abtest/static/abtest_static_homepage.html"
    return render(request, template)


def ABTestThanksView(request):
    
    """
    Render Thanks Static
    :param request:
    :return:
    """
    
    template = "app_abtest/static/abtest_static_thanks.html"
    return render(request, template)


# CUSTOM ERROR PAGE

def error_404_view(request, exception):
    return render(request,'app_abtest/static/404.html', locals())

# ---------------------------


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
        raise PermissionDenied('Upss... Maaf, halaman ini hanya untuk staff')
    else:
        abtest_list_dashboard = Design.objects.all().order_by("-is_created")
        template = "app_abtest/dashboard/abtest_dashboard_list.html"
        paginator = Paginator(abtest_list_dashboard, 3)
        page = request.GET.get('page', 1)
        try:
            abtest_list_dashboard = paginator.page(page)
        except PageNotAnInteger:
            abtest_list_dashboard = paginator.page(1)
        except EmptyPage:
            abtest_list_dashboard = paginator.page(paginator.num_pages)
        context = {
            'abtest_list_dashboard': abtest_list_dashboard,
        }
        return render(request, template, context)


@login_required
def ABTestDetailDashboardView(request, pk):

    """
    Render Single A/B Test with Stats
    :param request:
    :param pk:
    :return:
    """
    
    if not request.user.is_staff:
        raise Http404("Page does not exist")
    abtest = Design.objects.get(pk=pk)
    abtest_results = DesignComment.objects.filter(design_abtest_title=abtest.id)
    template = "app_abtest/dashboard/abtest_dashboard_detail.html"
    total_ab = DesignComment.objects.filter(design_abtest_title=abtest.id).annotate(num_ab=Count('design_abtest_choice'))
    total_a = DesignComment.objects.filter(design_abtest_title=abtest.id, design_abtest_choice="a").annotate(num_a=Count('design_abtest_choice'))
    total_b = DesignComment.objects.filter(design_abtest_title=abtest.id, design_abtest_choice="b").annotate(num_b=Count('design_abtest_choice'))
    paginator = Paginator(abtest_results, 9)
    page = request.GET.get('page', 1)
    try:
        abtest_results = paginator.page(page)
    except PageNotAnInteger:
        abtest_results = paginator.page(1)
    except EmptyPage:
        abtest_results = paginator.page(paginator.num_pages)
    context = {
        'abtest': abtest, 
        'abtest_results': abtest_results,
        'total_ab': total_ab,
        'total_a': total_a,
        'total_b': total_b
    }
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
        raise Http404("Test does not exist")

    form = ABTestCommentModelForm(request.POST)
    template = "app_abtest/tester/abtest_tester_detail.html"
    context = {'abtest': abtest, 'form': form}
    if abtest.is_published != True and not request.user.is_staff:
        raise Http404("Page does not exist")
    if request.method == "POST":
        # yesterday = timezone.now() - timezone.timedelta(days=1)
        form = ABTestCommentModelForm(request.POST)
        if form.is_valid():
            result = form.save(commit = False)
            result.design_abtest_title = Design.objects.get(design_title=abtest.design_title)
            result.design_abtest_tester_user = Tester.objects.get(user=request.user)
            result.design_abtest_tester_email = request.user.email
            result.is_created = datetime.now()
            result.abtest = abtest
            result.save()
            return HttpResponseRedirect('/thanks/') #Nanti harus thank you page
    else:
        form = ABTestCommentModelForm()
    return render(request, template, context)

# ---------------------------