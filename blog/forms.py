from dataclasses import field
from django import forms
from django.core.exceptions import ValidationError

from .models import Tag, Post


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
 
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug must be an unique. We have "{new_slug}" slug already.')
        return new_slug 


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'body': forms.Textarea(attrs={'class': 'form-control mb-2'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-select mb-2' })
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
 
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug