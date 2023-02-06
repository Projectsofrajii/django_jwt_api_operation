from rest_framework import serializers
from .models import RsmRoleMaster ,RsmUserMaster
from model_utils import Choices

class RsmUserMasterSeri(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)

    class Meta:
        model = RsmUserMaster
        fields = ('user_id', 'user_name', 'password', 'email_id', 'mobile',
                  'role', 'status', 'type', 'updated_timestamp')

    def validate(self, args):
        username = args.get('user_name', None)
        email = args.get('email_id', None)
        mobile = args.get('mobile', None)

        if RsmUserMaster.objects.filter(user_name=username).exists():
            raise serializers.ValidationError({
                'Message': [{'user_name': 'Already Exists'}]
            })

        if RsmUserMaster.objects.filter(email_id=email).exists():
            raise serializers.ValidationError({
                'Message': [{'email': 'Already Exists'}]
            })

        if not len(mobile) == 10:
            raise serializers.ValidationError({
                'Message': [{'Contact': 'Phone Number should maximum 10 digit', }]
            })

        return super().validate(args)

class RsmRoleMasterSeri(serializers.ModelSerializer):
    role_id = serializers.CharField()
    role_description = serializers.CharField()
    role_type = serializers.CharField()

    class Meta:
        model = RsmRoleMaster
        fields = ('role_id', 'role_description', 'role_type')

class RsmUserUpdateSeri(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)

    class Meta:
        model = RsmUserMaster
        fields = ('user_id', 'user_name', 'password', 'email_id', 'mobile',
                  'role', 'status', 'type', 'updated_timestamp')
#work only on view & update