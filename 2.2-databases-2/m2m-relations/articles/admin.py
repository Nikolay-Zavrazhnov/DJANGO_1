from django.contrib import admin

from .models import Article, Tag, Scope

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):

    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') is True:
                count += 1

        if count > 1:
            raise ValidationError('Основным может быть только один раздел')
        if count == 0:
            raise ValidationError('Укажите основной раздел')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [RelationshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']