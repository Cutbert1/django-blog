from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for adding comments on blog post.
    """
    class Meta:
        model = Comment
        fields = ('body',)
