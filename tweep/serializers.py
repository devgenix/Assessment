# Rest framework Imports
from rest_framework import serializers

# Own Imports
from tweep.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    
    time_created = serializers.SerializerMethodField()
    
    class Meta:
        model = Tweet
        fields = "__all__"
        read_only_fields = ["time_created"]
    
    def get_time_created(self, obj) -> str:
        time_created = obj.time_created.time().strftime('%H:%M:%S') 
        return time_created