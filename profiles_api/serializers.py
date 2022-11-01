from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10,)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs ={ 
            'passwords':{
                'write_only':True,
                'style':{
                    'input':'password',
                }
            }
        }
    def create(self,validation_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validation_data['email'],
            name = validation_data['name'],
            password = validation_data['password']
        )

        return user














