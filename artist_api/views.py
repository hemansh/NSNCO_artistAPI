from django.shortcuts import render
from .models import Artist,Work
from .serialize import ArtistSerializer,WorkSerializer
from rest_framework import generics,permissions,status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serialize import UserSerializer

class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        artist = Artist.objects.get(name=self.request.user)
        instance = serializer.save()
        artist.work.add(instance)

class ArtistWorkListView(generics.ListAPIView):
    def get_serializer_class(self):
        if 'artist' in self.request.query_params:
            return ArtistSerializer
        elif 'work_type' in self.request.query_params:
            return WorkSerializer
        else:
            return ArtistSerializer

    def get_queryset(self):
        artist_name = self.request.query_params.get('artist','DEFAULT_VALUE')
        if artist_name != 'DEFAULT_VALUE':
            res = Artist.objects.filter(name=artist_name)
            return res
        work_type = self.request.query_params.get('work_type','DEFAULT_VALUE')
        if work_type != 'DEFAULT_VALUE':
            return Work.objects.filter(workType=work_type)
        else:
            return Artist.objects.none
    
# class ArtistRegisterView(generics.CreateAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=user)
        headers = self.get_success_headers(serializer.data)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
    
class DelArtist(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

    def perform_destroy(self, instance):
        try:
            u = User.objects.get(username=self.request.user)
            u.delete()
            return "success"
        except:
            return "Error"
    

