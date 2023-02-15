from django import forms
from .models import Blog,Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']


class NewBlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    url=forms.URLField(max_length=100)
    cat = forms.CharField(max_length=100)
    # img = forms.ImageField(upload_to='media/post/')



# Path: iblogs-main\iblogs-main\blog\urls.py
        
