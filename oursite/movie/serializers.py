from .models import Movies
from rest_framework import fields, serializers

class Sort(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url =True)
    class Meta:
        model = Movies
        fields = ['id', 'title','description', 'category','duration','rating', 'image']
