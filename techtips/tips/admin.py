# This file is part of Tech Tip of the Day.
# 
# Tech Tip of the Day is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tech Tip of the Day is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tech Tip of the Day.  If not, see <http://www.gnu.org/licenses/>.

from django.contrib import admin
from techtips.tips.models import Tip

class TipAdmin(admin.ModelAdmin):
    # List parameters
    list_display = ('title', 'created_at', 'created_by', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_by')
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

