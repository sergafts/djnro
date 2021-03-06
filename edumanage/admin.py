# -*- coding: utf-8 -*-.
from django.contrib import admin
from edumanage.models import (
    Name_i18n,
    URL_i18n,
    Contact,
    InstitutionContactPool,
    InstRealm,
    InstServer,
    InstRealmMon,
    MonProxybackClient,
    MonLocalAuthnParam,
    ServiceLoc,
    Institution,
    InstitutionDetails,
    Realm,
    RealmData,
    CatEnrollment
)

from django.contrib.contenttypes import generic


class NameInline(generic.GenericTabularInline):
    model = Name_i18n


class UrlInline(generic.GenericTabularInline):
    model = URL_i18n


class InstitutionAdmin(admin.ModelAdmin):
    inlines = [
        NameInline,
    ]


class InstitutionDetailsAdmin(admin.ModelAdmin):
    inlines = [
        UrlInline,
    ]


class ServiceLocAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'institutionid')
    inlines = [
        NameInline,
    ]


class RealmInLine(admin.ModelAdmin):
    inlines = [
        UrlInline, NameInline
    ]


class InstRealmAdmin(admin.ModelAdmin):
    list_display = ('realm', 'instid')


class CatEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'cat_active')

admin.site.register(Name_i18n)
admin.site.register(Contact)
admin.site.register(InstitutionContactPool)
admin.site.register(URL_i18n)
admin.site.register(InstRealm, InstRealmAdmin)
admin.site.register(InstServer)
admin.site.register(InstRealmMon)
admin.site.register(MonProxybackClient)
admin.site.register(MonLocalAuthnParam)
admin.site.register(ServiceLoc, ServiceLocAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(InstitutionDetails, InstitutionDetailsAdmin)
admin.site.register(Realm, RealmInLine)
admin.site.register(RealmData)
admin.site.register(CatEnrollment, CatEnrollmentAdmin)

from django import forms
from django.core.urlresolvers import reverse
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

from django.contrib import admin

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
