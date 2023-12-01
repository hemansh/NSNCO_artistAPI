from rest_framework import serializers
from .models import Artist, Work
from django.contrib.auth.models import User

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id','link','workType']

class ArtistSerializer(serializers.ModelSerializer):
    # work = WorkSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['id','name','work']
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password','first_name','last_name', 'email']
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
