from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

from django.conf import settings


class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = [
            settings.MEDIA_URL + 'js/cleditor/jquery.cleditor.min.js',
            settings.MEDIA_URL + 'js/cleditor/jquery.cleditor.advancedtable.min.js',
            #settings.MEDIA_URL + 'js/cleditor/jquery.cleditor.bbcode.min.js',
            #settings.MEDIA_URL + 'js/cleditor/jquery.cleditor.icon.min.js',
            settings.MEDIA_URL + 'js/cleditor/cleditor.js']
        css = {'all': (settings.MEDIA_URL + 'js/cleditor/jquery.cleditor.css',)}


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
