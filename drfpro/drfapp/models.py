from django.db import models

from django.contrib.auth import models as auth_models
from model_utils import Choices

class RsmUserMaster(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=45)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=128, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='EMAIL_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='ROLE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    updated_timestamp = models.DateTimeField(db_column='UPDATED_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RSM_USER_MASTER'


class RsmRoleMaster(models.Model):

    role_id = models.AutoField( primary_key=True)
    role_description = models.CharField( max_length=45, blank=True, null=True)
    role_type = models.CharField( max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RSM_ROLE_MASTER'
'''
from django.db import models
from model_utils import Choices


class Manager(models.Model):

    def create_user(self, user_id: int, user_name: str, password: str, email_id: str, mobile: str, role: str,
                    status: str,
                    type: str):

        if not user_id:
            raise ValueError('Users must have an user_id')

        if not user_name:
            raise ValueError('Users must have an user_name')

        if not password:
            raise ValueError('Users must have an password')

        if not email_id:
            raise ValueError('Users must have an email_id')

        if not role:
            raise ValueError('Users must have an role')

        if not status:
            raise ValueError('Users must have an status')

        if not type:
            raise ValueError('Users must have an type')

        user = self.model(email_id=self.normalize_email(email_id))
        user.user_id = user_id
        user.user_name = user_name
        user.mobile = mobile
        user.set_password(password)
        user.is_admin = False
        user.role = role
        user.status = status
        user.type = type
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, user_name: str, email_id: str, password: str, mobile: str, status: str,
                         type: str) -> "User":

        user = self.create_user(user_name=user_name, email_id=email_id, password=password,
                                mobile=mobile, status=status, type=type)
        user.role = 'SuperUser'
        user.save()
        return user


class RsmUserMaster(models.Model):
    user_id = models.AutoField(primary_key=True, max_length=45)
    user_name = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    email_id = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    STATUS = Choices('SuperUser', 'User', 'Quest', )
    role = models.CharField(choices=STATUS, default=STATUS.Quest, max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    updated_timestamp = models.DateTimeField(blank=True, null=True)
    access_token = models.CharField(max_length=500, blank=True, null=True)

    USERNAME_FIELD = 'email_id'
    REQUIRED_FIELDS = ['user_name', 'mobile']

    class Meta:
        managed = False
        db_table = 'rsmusermaster'


class RsmRoleMaster(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_description = models.CharField(max_length=45, blank=True, null=True)
    role_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rsmrolemaster'

    def user(self, email_id: str, password: str):
        user = self.model(email_id=email_id)
        user.set_password(password)

'''