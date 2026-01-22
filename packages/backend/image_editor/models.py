from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class PromptTemplate(models.Model):
    name = models.CharField(max_length=100)
    prompt_text = models.TextField()
    preview_image = CloudinaryField('image', folder="previews/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name