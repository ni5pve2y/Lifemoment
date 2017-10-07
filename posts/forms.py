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


class SearchForm(forms.Form):
    title = forms.CharField(max_length=150)
