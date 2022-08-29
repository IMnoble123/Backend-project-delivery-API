from . models import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

        fields = ['id','username','email','mobile','is_active','password']
        extra_kwargs={'email':{'required':True},'password': {'write_only': True},'is_active':{'read_only' : True}}

    def create(self, validated_data):
        user = Account(
                email      = validated_data['email'],
                mobile     = validated_data['mobile'],
                
            )
        user.set_password(validated_data['password'])
        user.save()
        return user
