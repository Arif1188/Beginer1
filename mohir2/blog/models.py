from django.db import models

# Create your models here.

class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    made_in = models.CharField(max_length=100)
    made_year = models.DateField()
    product_color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products_image')
    company_email = models.EmailField(null=True, blank=True)
    product_link = models.URLField(null=True,blank=True)
    
    def __str__(self) -> str:
        return f"{self.product_name} {self.made_in}"
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    
