from urllib.parse import urlparse

from rest_framework import serializers

from config import settings


class VideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        domain = urlparse(value.get('video_url')).netloc
        if domain not in [settings.BASE_URL, 'www.youtube.com', 'youtube.com']:
            raise serializers.ValidationError("It's not possible to use a link from this resource")

