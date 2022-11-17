from django.contrib import admin
from .models import *


class WhatYouLearnInline(admin.TabularInline):
    model = WhatYouLearn


class RequirementsInline(admin.TabularInline):
    model = Requirements


class VideoInline(admin.TabularInline):
    model = Video


# @admin.register(Categories)
# class CategoriesAdmin(admin.ModelAdmin):
#     list_display = ('name', 'icon')


# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'about_author')


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'category', 'status', 'level', 'created_at')
#     inlines = (WhatYouLearnInline, RequirementsInline, VideoInline)


class CourseAdmin(admin.ModelAdmin):
    inlines = (WhatYouLearnInline, RequirementsInline, VideoInline)


admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Level)
admin.site.register(Course, CourseAdmin)
admin.site.register(WhatYouLearn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Language)
