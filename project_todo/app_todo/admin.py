from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdminModel(admin.ModelAdmin):
    list_display= ('user','title','description','created')


admin.site.register(Task,TaskAdminModel)
