from django.contrib import admin

from apps.codeAnalyzer.models import Archive, Problems

# Register your models here.
admin.site.register(Archive)
admin.site.register(Problems)