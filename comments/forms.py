from django import forms
from .models import Comments


class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['username', 'email', 'comment_text']
