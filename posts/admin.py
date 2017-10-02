from django.contrib import admin

from posts.models import Post, Comment


class PostProfileAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'timestamp',
        'edited',
    )

    list_filter = (
        'timestamp',
        'edited',
        'user',
        'slug',
    )


class CommentProfileAdmin(admin.ModelAdmin):
    list_display = (
        'context',
        'post',
        'user',
        'timestamp',
        'edited',
    )

    list_filter = (
        'timestamp',
        'edited',
        'user',
    )


admin.site.register(Post, PostProfileAdmin)
admin.site.register(Comment, CommentProfileAdmin)
