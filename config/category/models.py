from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent =models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True, blank=True, 
        related_name='children', 
    )

    def __str__(self) -> str:
        return self.name 
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural = 'Categories'