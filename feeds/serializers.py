from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer

class FeedSerializer(ModelSerializer):

    user=FeedUserSerializer(read_only=True) # feed 의 user모델을 직렬화 하기 위해 필요한 코드

    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1 #유저 정보 모두 보여줌