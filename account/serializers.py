from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from . models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['blockchain_address'] = user.blockchain_address
        token['eval_test'] = user.eval_test
        token['is_admin'] = user.is_admin
        token['is_active'] = user.is_active
        
        return token
    
# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name" , "sex", "blockchain_address" ,"is_user", "eval_test", "password"]
        read_only_fields = ["is_user", "eval_test", "blockchain_address"]
        extra_kwargs = {
                    'password': {'write_only': True}
                }
        
    def create(self, validated_data):
        user = User.objects.create(
                    email=validated_data['email'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    sex=validated_data['sex'],
                    blockchain_address=validated_data.get('blockchain_address'),
                    is_user=True,
                    eval_test = False,
                )
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    # set email to read only on update
    def get_fields(self):
        fields = super().get_fields()
        if self.instance:
            fields['email'].read_only = True
        return fields
    
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ["id", "email", "first_name", "last_name" , "sex", "blockchain_address" ,"is_user"]
        read_only_fields = ["email", "blockchain_address" ,"is_user"]
        
        
class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True)
    
    
class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()