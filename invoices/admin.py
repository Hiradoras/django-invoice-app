from django.contrib import admin
from .models import Invoice, Tag
from import_export import resources
from import_export.admin import ExportActionMixin


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TagResource

admin.site.register(Invoice)
admin.site.register(Tag, TagAdmin)
