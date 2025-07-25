from django.db import models

# Create your models here.
class Story(models.Model):
    good_moral = models.CharField(max_length=255, blank=True)
    bad_moral = models.CharField(max_length=255, blank=True)
    story_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Story ({self.good_moral} / {self.bad_moral})"

