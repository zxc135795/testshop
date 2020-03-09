from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Good)

admin.site.register(ShoeTime)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Youther)
admin.site.register(CategoryShow)
admin.site.register(ToImg)



