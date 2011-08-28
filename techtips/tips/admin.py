from django.contrib import admin
from techtips.tips.models import Tip

class TipAdmin(admin.ModelAdmin):
    # List parameters
    list_display = ('title', 'created_at', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    date_hierarchy = 'created_at'
    search_fields = ('title', 'content_markdown')
    
    # Detail parameters
    fields = ('title', 'slug', 'content_markdown', 'is_published', 
              'created_at', 'created_by')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'created_by')
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
    

admin.site.register(Tip, TipAdmin)
