from django import forms
from .models import DesignComment


class ABTestCommentModelForm(forms.ModelForm):

    """
    Comment Form
    """

    class Meta:
        model = DesignComment
        fields = (
            'design_abtest_tester_name',
            'design_abtest_choice',
            'design_abtest_comment'
        )
        exclude = [ 'design_abtest_title', 'design_abtest_tester_user', 'is_published']
        widgets = {
            'design_abtest_title': forms.HiddenInput(),
            'design_abtest_tester_user': forms.HiddenInput(),
            'is_published': forms.HiddenInput(),
            'design_abtest_choice': forms.RadioSelect()
        }

