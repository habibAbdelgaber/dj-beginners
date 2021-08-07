from django import forms
from .models import Post




class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=250, label='', widget=forms.TextInput(attrs={'placeholder': 'Write post title here...', 'class': 'form-control'}))
    content = forms.CharField(max_length=250, label='', widget=forms.Textarea(attrs={'placeholder': 'Write post content here...', 'class': 'form-control mt-1'}))
    class Meta:
        model = Post
        # fields = '__all__'
        # exclude = ['author']
        fields = ['title', 'content']

        labels = {
            'title': 'Write post title here...',
            'content': 'Write a post here...'
        }

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            for name, field in fields.items():
                field.widget.attrs.update({'input': 'form-control'})