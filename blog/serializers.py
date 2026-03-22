from rest_framework import serializers
from .models import Article 

#Serializer for Article model

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article 
        fields = "__all__"

        #validation globale 
        def validate(self,  data):
            if not data.get('title'):
                raise serializers.ValidationError("the title is required")
            if not data.get('autor'):
                raise serializers.ValidationError("the autor ")
