from django import forms

from captcha.fields import CaptchaField

from .models import Comment


class SearchForm(forms.Form):
    query = forms.CharField(label='')


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ('user_name', 'body')
