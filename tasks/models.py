from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUserInfoModel(AbstractUser):
    
    USER_TYPES ={
        ('seller','seller'),
        ('buyer','buyer'),
        
    }
    full_name = models.CharField(max_length=200,null=True)
    user_type = models.CharField(max_length=200,null=True,choices=USER_TYPES)
    
    def __str__(self):
        return f'{self.username}-{self.full_name}'
    
    
class TaskModel(models.Model):
    
    STATUS = {
        ('pending','pending'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
        ('Canceled','Canceled'),
    }
    
    title = models.CharField(max_length=200, null=True)
    description=models.TextField(null=True)
    status=models.CharField(max_length=20,choices=STATUS,null=True)
    due_date=models.DateField(null=True)
    created_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)
    created_by=models.ForeignKey(CustomUserInfoModel,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f'{self.title}'

    
class ProfileModel(models.Model):
    
    user = models.OneToOneField(CustomUserInfoModel,on_delete=models.CASCADE,related_name="user_profile")
    
    address = models.TextField(null=True)
    contact = models.CharField(max_length=20,null=True)
    image = models.ImageField(upload_to='media/profile_img',null=True)
    date_of_birth=models.DateField(null=True)
    
    def __str__(self):
        return f'{self.user.full_name}'
    
    
    
    ## productmodel : 
    
    
class ProductModel(models.Model):
        name=models.CharField(max_length=200,null=True)
        description = models.TextField(null=True)
        price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
        qty=models.PositiveIntegerField(null=True)
        total_amount=models.DecimalField(max_digits=10,decimal_places=2,null=True)
        created_by = models.ForeignKey(
            CustomUserInfoModel,
            on_delete=models.CASCADE,
            null=True,
            related_name='user_product',
        )
        
        created_at = models.DateTimeField(auto_now_add=True,null=True)
        updated_at = models.DateTimeField(auto_now=True,null=True)
        
        
        def __str__(self):
            return'f{self.name}'
        
