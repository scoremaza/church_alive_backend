import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.enums import Choices, ChoicesMeta
from django.db.models.fields.related import ForeignKey
from django.utils.deconstruct import deconstructible


@deconstructible
class GenerateProfileImagePath(object):
    '''
    This will allow naming convention for the files and up loaded
    as images in profiles. Image will have this assigned to its 
    upload_to property    
    '''
    
    def __init__(self) -> None:
        pass
    
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'media/accounts/{instance.user.id}/images'
        name = f'profile_image.ext'
        return os.path.join(path, name)
 
 
user_profile_image_path = GenerateProfileImagePath()   


class PositionType(models.Model):
    '''
    Model definition for PositionType
    Here the user is assign a position within the organization 
    allowing access and assignment capabilities enabling allocation
    throughout the system.
    '''
    position_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField(max_length=150)
    sort_order = models.IntegerField(default=-1)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """Meta definition for VisibilityLevel."""
        
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        """Unicode representation of VisibilityLevel."""
                     
        return f'{self.position}'

    def get_absolute_url(self):
        """Return absolute url for VisibilityLevel."""
        
        pass
    
    
class Profile (models.Model):
    '''
    Model definition for Profile
    Here the user will create its existence in the appplication
    with features to set privacy and adding friends will be 
    controlled by this profile. Using User from the internal structure 
    of Django as the manager to keep things together. 
    '''
    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_profile_image_path, blank=True, null=True)
    profile_name = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    position_type = models.ForeignKey(PositionType, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for VisibilityLevel."""
        
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """Unicode representation of VisibilityLevel."""
         
        return f'{self.user.username}\'s Profile'

    def get_absolute_url(self):
        """Return absolute url for VisibilityLevel."""
        
        pass


class VisibilityLevel(models.Model):
    """
    Model definition for VisibilityLevel.
    Here the user will give wether a friend could have the 
    capabilities to view or send information. 
    """    

    visibility_level_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)

    class Meta:
        """Meta definition for VisibilityLevel."""

        verbose_name = 'VisibilityLevel'
        verbose_name_plural = 'VisibilityLevels'

    def __str__(self):
        """Unicode representation of VisibilityLevel."""
        return self.name


    def get_absolute_url(self):
        """Return absolute url for VisibilityLevel."""
        pass

    




class PrivacyFlagType(models.Model):
    '''
    Model definition for PrivacyFlagType.
    Here we have the values of information such as questions asked to the 
    user and the user answers will be stored in PrivacyFlag
    
    '''
    
    privacy_flag_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    field_name = models.CharField(max_length=150,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    sort_order = models.IntegerField(default=-1)

    class Meta:
        """Meta definition for VisibilityLevel."""
        
        verbose_name = "PrivacyFlagType"
        verbose_name_plural = "PrivacyFlagTypes"

    def __str__(self):
        """Unicode representation of VisibilityLevel."""
        
        return self.field_name

    def get_absolute_url(self):
        """Return absolute url for VisibilityLevel."""
        
        pass
    
    
class PrivacyFlag(models.Model):
    '''
    Model definition for PrivacyFlag
    Here we will allocate the values and controling what 
    could be seen and by whom. 
    '''
    privacy_flag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    privacyflagtype = models.ForeignKey(PrivacyFlagType, on_delete=models.CASCADE)
    visibility_level = models.ForeignKey(VisibilityLevel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """Meta definition for VisibilityLevel."""
        
        verbose_name = "PrivacyFlag"
        verbose_name_plural = "PrivacyFlags"

    def __str__(self):
        """Unicode representation of VisibilityLevel."""
        return f'{self.profile.user.username} has {self.privacyflagtype.field_name} privacy'

    def get_absolute_url(self):
        """Return absolute url for VisibilityLevel."""
        pass
 
 
class ProfileAttributeType(models.Model):
     '''
     Model definition for ProfileAttributeType
     Here we have the type of values enter by the user 
     '''
     profile_attribute_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     attribute_type =  models.CharField(max_length=500)
     sort_order = models.IntegerField(default=-1)
     privacy_flag_type = models.ForeignKey(PrivacyFlagType, on_delete=models.CASCADE)
     
     class Meta:
        """Meta definition for VisibilityLevel."""
         
        verbose_name = "ProfileAttributeType"
        verbose_name_plural = "ProfileAttributeTypes"

     def __str__(self):
        """Unicode representation of VisibilityLevel."""
        return f'{self.profile.user.username} has {self.privacyflagtype.field_name} privacy'

     def get_absolute_url(self):
        """Return absolute url for VisibilityLevel."""
        pass

    
class ProfileAttribute(models.Model):
    '''
    Model definition for ProfileAttribute.
    Here we have the values themselves given by the user 
    '''
    
    profile_attribute_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    profile_attribute_type = models.ForeignKey(ProfileAttributeType, on_delete=models.CASCADE)
    response = models.CharField(max_length=250)
    createDate = models.DateField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """Meta definition for VisibilityLevel."""
        
        verbose_name = "ProfileAttribute"
        verbose_name_plural = "ProfileAttributes"

    def __str__(self):
        """Unicode representation of VisibilityLevel."""
        return f'{self.profile.user.username} response {self.response}'

    def get_absolute_url(self):
        """Return absolute url for VisibilityLevel."""
        
        pass
    
    
class AlertType(models.Model):
    '''
    Model definition for  AlertType.
    Here we have the user with the capability to have alerts from different 
    news form their friends 
    '''
    
    alert_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    
    class Meta:
        """Meta definition for VisibilityLevel."""
        
        verbose_name = "AlertType"
        verbose_name_plural = "AlertTypes"

    def __str__(self):
        """Unicode representation of VisibilityLevel."""
        return f'{self.name}'

    def get_absolute_url(self):
        """Return absolute url for VisibilityLevel."""
        
        pass
   
    
class Alert(models.Model):
    '''
    Model definition for Alert.
    Here we have the whole set completion for the 
    Alerts. Allow the system to use the functionality 
    of hidding and allowing users to manage the completion
    of there news feed, with notifications.  
    
    '''
    
    alert_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    alert_type = models.ForeignKey(AlertType, on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=False)
    message = models.TextField()
    
    
    class Meta:
        """Meta definition for VisibilityLevel."""
        
        verbose_name = "Alert"
        verbose_name_plural = "Alerts"

    def __str__(self):
        """Unicode representation of VisibilityLevel."""    
        return f'{self.alert_type.name} has this {self.message}'

    def get_absolute_url(self):
        """Return absolute url for VisibilityLevel."""
        
        pass