from django.contrib import admin
from tasks.models import*

admin.site.register([CustomUserInfoModel,TaskModel])