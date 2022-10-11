from rest_framework import serializers
from .models import Banner

class BannerSerializer(serializers.ModelSerializer):

    link = serializers.SerializerMethodField('getLink')
    imageID = serializers.SerializerMethodField('getImageID')

    class Meta:
        model = Banner
        fields = ['id','imageID', 'name', 'link']

    def getLink(self, obj):
        return obj.image.url
    
    def getImageID(self, obj):
        return obj.image.name