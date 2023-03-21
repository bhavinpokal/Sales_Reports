from django.db import models
from django.urls import reverse

from profiles.models import Profile


class Report(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='reports', blank=True)
    remarks = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse("data_reports:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)
