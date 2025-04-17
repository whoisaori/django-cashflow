from django.contrib import admin
from .models import Type, Category, SubCategory, Status, Transaction


admin.site.register(Type)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Transaction)
admin.site.register(Status)
