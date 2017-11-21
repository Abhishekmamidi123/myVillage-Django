from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass', 'placeholder':'Title'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent', 'placeholder':'Description...'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass', 'placeholder':'Author'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea', 'placeholder':'Comment'}),
        }
        

