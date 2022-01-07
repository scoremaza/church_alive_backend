import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices, ChoicesMeta
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

class Profile (models.Model):
    '''
    Here the user will create its existence in the appplication
    with features to set privacy and adding friends will be 
    controlled by this profile.  
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_profile_image_path, blank=True, null=True)
    profile_name = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def get_absolute_url(self):
        pass


class PrivacyFlagType(models.Model):
    '''
    
    '''
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    field_name = models.CharField(max_length=150,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    sort_order = models.IntegerField(default=-1)

    class Meta:
        verbose_name = "PrivacyFlagType"
        verbose_name_plural = "PrivacyFlagTypes"

    def __str__(self):
        return self.field_name

    def get_absolute_url(self):
        pass
    
    
class PrivacyFlag(models.Model):
    '''
    Here we will allocate the situations of controling what 
    could be seen and by whom. 
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    privacyflagtype = models.ForeignKey(PrivacyFlagType, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "PrivacyFlag"
        verbose_name_plural = "PrivacyFlags"

    def __str__(self):
        return f'{self.profile.user.username} has {self.privacyflagtype.field_name} privacy'

    def get_absolute_url(self):
        pass