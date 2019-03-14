from django.db import models
from django.urls import reverse
from app_user.models import Tester
from taggit.managers import TaggableManager


class Design(models.Model):

    """
    Design/Materi Testing Model
    """
    
    id = models.AutoField(
        primary_key = True
    )

    design_title = models.CharField(
        verbose_name = "A/B Testing Title",
        max_length = 225,
        null = False,
        blank = False
    )

    design_image_a = models.ImageField(
        upload_to = 'images/%Y/%m/%d',
        null = True,
        blank = True
    )

    design_image_b = models.ImageField(
        upload_to ='images/%Y/%m/%d',
        null = True,
        blank = True
    )

    is_published = models.BooleanField(
        default = False
    )

    is_created = models.DateTimeField(
        auto_now_add = True,
        null = True,
        blank = True
    )

    is_modified = models.DateTimeField(
        auto_now = True,
        null = True,
        blank = True
    )

    tags = TaggableManager()

    class Meta:
        verbose_name_plural = "Design Testing Materials"


    def __str__(self):
        return str(self.design_title)


class DesignComment(models.Model):

    """
    AB Test Comment Model
    """

    AB = (
        ('a', 'A'), 
        ('b', 'B')
    )

    design_abtest_tester_user = models.ForeignKey(
        Tester,
        verbose_name = "Tester user",
        related_name = 'tester_user_hook',
        null = True,
        blank = True,
        on_delete = models.CASCADE
    )

    design_abtest_title = models.ForeignKey(
        Design, 
        verbose_name = "Testing Title",
        related_name = "testing_title",
        null = True,
        blank = True,
        on_delete = models.CASCADE
    )

    design_abtest_tester_name = models.CharField(
        verbose_name = "Tester name",
        default = "Tester",
        max_length = 225,
        null = False,
        blank = False
    )

    design_abtest_choice = models.CharField(
        choices = AB,
        verbose_name = "A/B?",
        null = True,
        blank = False,
        max_length=1
    )

    design_abtest_comment = models.TextField(
        verbose_name = "Comment",
        null = False,
        blank = False
    )

    is_published = models.BooleanField(
        default = False
    )

    is_created = models.DateTimeField(
        auto_now_add = True,
        null = True,
        blank = True
    )

    is_modified = models.DateTimeField(
        auto_now = True,
        null = True,
        blank = True
    )

    # Limit user only can post once
    # def save(self, *args, **kwargs):
    #     if self.__class__.objects.filter(design_abtest_tester_user=self.design_abtest_tester_user).count()>=1:
    #         return None
    #     return super().save(*args, **kwargs) 

    class Meta:
        verbose_name_plural = "Test Results"

    def __str__(self):
        return str(self.design_abtest_tester_name)