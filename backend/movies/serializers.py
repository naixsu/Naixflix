from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)

        return movie
