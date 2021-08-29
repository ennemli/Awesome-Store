from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
class ShopByDepartment(models.Model):
    name=models.CharField(max_length=250,unique=True)
    class Meta:
        order_with_respect_to="name"
    def __str__(self):
        return self.name
class ProductCategory(models.Model):
    name=models.CharField(max_length=250,unique=True)
    shopbydepartment=models.ManyToManyField(ShopByDepartment)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=256)
    product_title=models.CharField(max_length=256)
    product_description=models.TextField()
    product_image=models.ImageField()
    category=models.ManyToManyField(ProductCategory)
    class Meta:
        order_with_respect_to="product_name"
    def __str__(self):
        return self.product_name
class CustomAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,username,birthday,password,
                    is_superuser=False):
        if not email:
            raise ValueError('You must provide an email')
        email=self.normalize_email(email)
        user=self.user = self.model(
            first_name=first_name, last_name=last_name, email=email,
            username=username, birthday=birthday,is_superuser=is_superuser)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,first_name,last_name,email,username,birthday,password):
        return self.create_user(first_name,last_name,email,username,birthday,password,
                                is_superuser=True)


class User(AbstractBaseUser,PermissionsMixin):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100,blank=False)
    last_name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(blank=False,unique=True)
    username=models.CharField(max_length=150,unique=True)
    birthday=models.DateField(blank=False)
    password=models.CharField(max_length=150,blank=False)
    objects=CustomAccountManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['first_name','last_name','username','birthday']
    def __str__(self):
        return self.email
    @property
    def is_staff(self):
        return self.is_superuser


