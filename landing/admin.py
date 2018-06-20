from django.contrib import admin
from .models import *


class SubscriberAdmin (admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Subscriber._meta.fields]
    # exclude = ["email"]
    #   исключает указанное поле
    list_filter = ["name"]
    #  добовляет фильтыр
    search_fields = ["name", "email"]
    #  добовляет поиск
    fields = ["email"]


admin.site.register(Subscriber, SubscriberAdmin)
