from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe
from tzwapp.models import Category, Course, Lesson, Tag
from django import forms
from django.urls import path
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

    @staticmethod
    def image_view(lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width='200' />")


class MyAdminSite(admin.AdminSite):
    site_header = 'OU Online Course'

    def get_urls(self):
        return [path('course_stats/', self.course_stats)] + super().get_urls()

    def course_stats(self, request):
        stats = Category.objects.annotate(course_count=Count('course__id')).values('id', 'name', 'course_count')

        return TemplateResponse(request, 'admin/course_stats.html', {
            'stats': stats
        })


admin_site = MyAdminSite(name='TZW_Course')


admin_site.register(Category)
admin_site.register(Course)
admin_site.register(Lesson, MyLessonAdmin)
admin_site.register(Tag)
