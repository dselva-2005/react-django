from rest_framework import serializers

class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True,source='public_id',format='hex')
    updated = serializers.DateTimeField(read_only=True)
    created = serializers.DateTimeField(read_only=True)