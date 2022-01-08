from django.contrib import admin
from .models import Profile, ProfileAttribute, \
    ProfileAttributeType, PrivacyFlag, PrivacyFlagType, VisibilityLevel,\
    Alert, AlertType, PositionType


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('profile_id', 'create_date')


@admin.register(ProfileAttribute)
class ProfileAttributeAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'create_date')


@admin.register(PositionType)
class PositionTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('position_id', 'create_date')


@admin.register(PrivacyFlagType)
class PrivacyFlagType(admin.ModelAdmin):
    readonly_fields = ('privacy_flag_type_id', 'create_date')


@admin.register(PrivacyFlag)
class PrivacyFlagAdmin(admin.ModelAdmin):
    readonly_fields = ('privacy_flag_id', 'create_date')


@admin.register(ProfileAttributeType)
class ProfileAttributeTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('profile_attribute_type_id', 'create_date')


@admin.register(AlertType)
class AlertTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('alert_type_id', 'create_date')


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    readonly_fields = ('alert_id', 'create_date')


@admin.register(VisibilityLevel)
class VisibilityLevelAdmin(admin.ModelAdmin):
    readonly_fields = ('visibility_level_id', 'create_date')
