from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    tags_csv = forms.CharField(
        label='Tags (comma separated)',
        required=False,
        help_text='e.g. django, python'
    )

    class Meta:
        model = Post
        fields = ['title', 'body', 'published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['tags_csv'].initial = ', '.join(t.name for t in self.instance.tags.all())

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            # set tags
            names = [s.strip() for s in self.cleaned_data.get('tags_csv','').split(',') if s.strip()]
            from .models import Tag
            tags = []
            for n in names:
                tag, _ = Tag.objects.get_or_create(name=n)
                tags.append(tag)
            instance.tags.set(tags)
        return instance

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3})
        }
