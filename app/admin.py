from django.contrib import admin

# Register your models here.
from .models import User,ShopByDepartment,ProductCategory,Product
class ProductCategoryAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass
class ShopByDepartmentAdmin(admin.ModelAdmin):
    pass
class UserAdmin(admin.ModelAdmin):
    exclude = ("password",)

admin.site.register(User,UserAdmin)

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(ShopByDepartment,ShopByDepartmentAdmin)
