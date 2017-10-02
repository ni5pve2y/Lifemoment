from django import forms

from posts.models import Post, Comment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'context',
            'image',
        )


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'context',
        )
