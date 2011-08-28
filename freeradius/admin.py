# -*- coding: utf-8 -*-
from django.contrib import admin

from freeradius.models import Attributelist
from freeradius.models import Nas
from freeradius.models import Radpostauth
from freeradius.models import Realmgroup
from freeradius.models import Realms
from freeradius.models import Radreply
from freeradius.models import Radusergroup
from freeradius.models import Radcheck
from freeradius.models import Radgroupcheck
from freeradius.models import Radgroupreply
from freeradius.models import Radippool
from freeradius.models import Radacct


class AttributelistAdmin(admin.ModelAdmin):
    list_display   = ('attribute', 'enabled', 'checkitem',)
    list_filter    = ('enabled', 'checkitem',)
    ordering       = ('attribute', )
    search_fields  = ('attribute',)

class NasAdmin(admin.ModelAdmin):
    list_display   = ('nasname', 'shortname', 'type', 'ports', 'naslocation',)
    list_filter    = ('type', 'naslocation',)
    ordering       = ('nasname', )
    search_fields  = ('nasname', 'shortname', 'ports', 'naslocation',)

class RadpostauthAdmin(admin.ModelAdmin):
    pass

class RealmgroupAdmin(admin.ModelAdmin):
    pass

class RealmsAdmin(admin.ModelAdmin):
    pass

class RadreplyAdmin(admin.ModelAdmin):
    list_display   = ('calledstationid', 'custid', 'username', 'attribute', 'op', 'value',)
    list_filter    = ('calledstationid', 'custid', 'username',)
    search_fields  = ('attribute', 'value',)

class RadusergroupAdmin(admin.ModelAdmin):
    list_display   = ('groupname', 'username',)
    list_filter    = ('groupname',)
    search_fields  = ('username',)

class RadcheckAdmin(admin.ModelAdmin):
    list_display   = ('username', 'attribute', 'op', 'value',)
    list_filter    = ('username',)
    search_fields  = ('attribute', 'value',)

class RadgroupcheckAdmin(admin.ModelAdmin):
    list_display   = ('groupname', 'attribute', 'op', 'value',)
    list_filter    = ('groupname',)

class RadgroupreplyAdmin(admin.ModelAdmin):
    list_display   = ('groupname', 'attribute', 'op', 'value',)
    list_filter    = ('groupname',)

class RadippoolAdmin(admin.ModelAdmin):
    list_display   = ('pool_name', 'framedipaddress', 'nasipaddress', 'expiry_time',)
    list_filter    = ('pool_name', 'nasipaddress', 'expiry_time',)
    search_fields  = ('framedipaddress',)

class RadacctAdmin(admin.ModelAdmin):
    list_display   = ('acctuniqueid', 'username', 'nasipaddress', 'acctstarttime', 'acctsessiontime',)
    list_filter    = ('nasipaddress',)


admin.site.register(Attributelist,AttributelistAdmin)
admin.site.register(Nas,NasAdmin)
admin.site.register(Radpostauth,RadpostauthAdmin)
admin.site.register(Realmgroup,RealmgroupAdmin)
admin.site.register(Realms,RealmsAdmin)
admin.site.register(Radreply,RadreplyAdmin)
admin.site.register(Radusergroup,RadusergroupAdmin)
admin.site.register(Radcheck,RadcheckAdmin)
admin.site.register(Radgroupcheck,RadgroupcheckAdmin)
admin.site.register(Radgroupreply,RadgroupreplyAdmin)
admin.site.register(Radippool,RadippoolAdmin)
admin.site.register(Radacct,RadacctAdmin)



