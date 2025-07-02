from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    is_removed = models.BooleanField(default=False)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title