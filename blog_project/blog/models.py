from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=1024)
    body = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title