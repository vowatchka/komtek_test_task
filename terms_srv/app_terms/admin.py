from django.contrib import admin

from .models import Directory, DirectoryVersion, DirectoryItem


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    pass


@admin.register(DirectoryVersion)
class DirectoryVersionAdmin(admin.ModelAdmin):
    pass


@admin.register(DirectoryItem)
class DirectoryItemAdmin(admin.ModelAdmin):
    pass
