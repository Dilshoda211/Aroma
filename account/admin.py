from django.contrib import admin
from .models import User,Address
from django.utils.html import format_html


admin.site.register(Address)

@admin.register(User)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'image_tag')
    search_fields = ('username', )
    # list_filter = ('created_at', 'category')
    readonly_fields = ('image_tag',)
    def image_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover;" />', obj.photo.url)
        return "-"
    image_tag.short_description = "Rasm"