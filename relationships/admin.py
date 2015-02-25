from django.contrib import admin, auth
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User as DefaultUserModel

from .compat import AUTH_USER_MODEL
from .forms import RelationshipStatusAdminForm
from .models import Relationship, RelationshipStatus


class RelationshipInline(admin.TabularInline):
    model = Relationship
    raw_id_fields = ('from_user', 'to_user')
    extra = 1
    fk_name = 'from_user'


class UserRelationshipAdminMixin(object):
    inlines = (RelationshipInline,)


class RelationshipStatusAdmin(admin.ModelAdmin):
    form = RelationshipStatusAdminForm


if AUTH_USER_MODEL == 'auth.User':
    class UserRelationshipAdmin(UserRelationshipAdminMixin, UserAdmin):
        pass

    admin.site.unregister(auth.models.User)
    admin.site.register(auth.models.User, UserRelationshipAdmin)

admin.site.register(RelationshipStatus, RelationshipStatusAdmin)
