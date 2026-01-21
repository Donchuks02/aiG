from django.db import models

# Create your models here.

class PromptTemplate(models.Model):
    prompt_text = models.TextField()
    preview_image = models.ImageField(upload_to='templates/')
    
    created_at = models.DateTimeField(auto_now_add=True)