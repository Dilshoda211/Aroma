from django.contrib import admin
from django.utils.html import format_html
from .models import BlogCategory, BlogPost, BlogComment

# BlogCategory admin
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)


# BlogPost admin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'created_at', 'image_tag')
    search_fields = ('title', 'author__username', 'category__name')
    list_filter = ('created_at', 'category')
    readonly_fields = ('image_tag',)
    prepopulated_fields = {"slug": ("title",)}  # avtomatik slug hosil qilish

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover;" />', obj.image.url)
        return "-"
    image_tag.short_description = "Rasm"


# BlogComment admin
@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_at')
    search_fields = ('user__username', 'post__title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
