from django.db import models
from django.contrib.auth.models import User


class Tester(models.Model):

    """
    Tester Model
    """

    user = models.OneToOneField(
        User,
        verbose_name = "Tester",
        on_delete = models.CASCADE
    )

    tester_name = models.CharField(
        verbose_name = "Tester Name",
        max_length = 128,
        null = True,
        blank = False
    )

    def __str__(self):
        return str(self.user)
