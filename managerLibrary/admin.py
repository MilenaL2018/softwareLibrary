from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Principal)
admin.site.register(Preceptor)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Phone)
admin.site.register(CourseHistory)
admin.site.register(AcademicHistory)
admin.site.register(Grades)
admin.site.register(Presence)
admin.site.register(CustomUser)