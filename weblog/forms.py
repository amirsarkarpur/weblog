from django import forms
from .models import Comment

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_name', 'post', 'author', 'Comment_text', 'star', 'replay_comment']

    def clean_star(self):
        star = self.cleaned_data.get('star')
        try:
            star = int(star)  # تبدیل به عدد صحیح
        except (TypeError, ValueError):
            raise forms.ValidationError("امتیاز باید عددی صحیح باشد.")
        if star < 1 or star > 5:
            raise forms.ValidationError("امتیاز باید بین 1 و 5 باشد.")
        return star
