from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Tester(models.Model):

    """
    Tester Model
    """

    user = models.OneToOneField(
        User,
        default = "Tester",
        verbose_name = "Tester Username",
        on_delete=models.CASCADE
    )

    tester_name = models.CharField(
        verbose_name = "Tester Name",
        max_length = 128,
        null = True,
        blank = False
    )

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_tester(sender, instance, created, **kwargs):
    """
    Automatically Create User when Login
    """
    if created:
        Tester.objects.create(user=instance)

