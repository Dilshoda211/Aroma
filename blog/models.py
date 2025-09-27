from django.db import models
from account.models import User


class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def __str__(self) -> str:
        return self.name
class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,
                               related_name="posts")
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image =  models.ImageField(upload_to="Images/blogs/")
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE,related_name="posts")
    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self) -> str:
        return self.title

class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Blog comment"
        verbose_name_plural = "Blog comments"


    def __str__(self) -> str:
        return f"{self.user.username} {self.post.title}"
