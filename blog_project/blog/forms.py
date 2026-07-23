from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']  # <- Имя поля из вашей модели Comment
        widgets = {
            'body': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Напишите комментарий...'}
            ),
        }
        labels = {
            'body': '',
        }