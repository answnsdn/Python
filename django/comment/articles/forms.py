from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['user', 'like_users', 'recommend']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        # fields = ['content']
        exclude = ['article', 'user']