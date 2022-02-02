from django.contrib import admin
from home.models import Team, Portfolio, Blog, Total, Aloqa


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'phone', 'image_tag']
    readonly_fields = ('image_tag',)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


class TotalAdmin(admin.ModelAdmin):
    list_display = ['n1', 'n2', 'n3', 'n4']


class AloqaAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'create_time', 'create_date']
    readonly_fields = ['name', 'subject', 'phone', 'create_time', 'create_date', 'ip']


admin.site.register(Aloqa, AloqaAdmin)
admin.site.register(Total, TotalAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
