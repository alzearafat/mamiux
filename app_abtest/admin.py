from django.contrib import admin
from app_abtest.models import Design, DesignComment
from django_summernote.admin import SummernoteModelAdmin



class ABTestAdmin(admin.ModelAdmin):

    """
    A/B Test in Admin
    """
    
    model = Design
    list_display = [
        'design_title',
        'is_created',
        'is_modified',
        'is_published'
    ]

    list_filter = (
        'is_created',
        'is_modified'
    )


class ABTestCommentAdmin(SummernoteModelAdmin):

    """
    A/B Test Comment in Admin
    """

    model = DesignComment
    list_display = [
        'design_abtest_title',
        'design_abtest_tester_user',
        'design_abtest_tester_name',
        'design_abtest_tester_phone',
        'design_abtest_tester_email',
        'design_abtest_choice',
        'is_created',
        'is_modified',
        'is_published'
    ]

    list_filter = (
        'is_created',
        'is_modified'
    )

    summernote_fields = '__all__'

admin.site.register(Design, ABTestAdmin)
admin.site.register(DesignComment, ABTestCommentAdmin)
