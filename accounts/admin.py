from django.contrib import admin
from django.utils.html import format_html

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="30" height="25"/>', obj.profile_image.url)
        else:
            return '-'
    image_preview.short_description = 'Image'
    list_display = ['user', 'full_name', 'email', 'image_preview']
    search_fields = ['user__username', 'full_name', 'email']

admin.site.register(UserProfile, UserProfileAdmin)