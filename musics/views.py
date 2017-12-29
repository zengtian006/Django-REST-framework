# from django.shortcuts import render
#
# from musics.models import Music
#
#
# # Create your views here.
# def hello_view(request):
#     musics = Music.objects.all()
#
#     return render(request, 'hello_django.html', {
#         'musics': musics,
#     })
from musics.models import Music
from musics.serializers import MusicSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
