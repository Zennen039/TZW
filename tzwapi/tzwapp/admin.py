from django.contrib import admin
from django.utils.safestring import mark_safe

from tzwapp.models import Category, Course, Lesson, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class MyLessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'active', 'course']
    search_fields = ['subject']
    list_filter = ['id', 'created_date']
    readonly_fields = ['image_view']
    form = LessonForm

    def image_view(self, lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width='200' />")


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, MyLessonAdmin)
admin.site.register(Tag)
