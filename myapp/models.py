from django.db import models

# Create your models here.
class Image(models.Model):

    photo = models.ImageField(upload_to='myimage')
    name = models.CharField(max_length=50,default="")
    file = models.FileField(upload_to='myfiles',blank=True, null=True)
    
    # date = models.DateTimeField(auto_now_add=True)
    
    
    
        
