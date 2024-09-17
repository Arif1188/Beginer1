from django.db import models

# Create your models here.


class StudendModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)
    about_me = models.TextField(null=True, blank=True)
    number = models.DecimalField(max_digits=5, decimal_places=3)
    urls = models.URLField()
    image = models.ImageField(upload_to='students_img/')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    