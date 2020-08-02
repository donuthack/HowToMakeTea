from rest_framework import serializers

# class TeaComponents(serializers.Serializer):
#     type = serializers.CharField(max_length=40)
#     water = serializers.IntegerField()
#     temp = serializers.IntegerField()
#     sugar = serializers.IntegerField()


class PrepareTea(serializers.Serializer):
    temp = serializers.IntegerField()
    adds = serializers.ListField(
        child=serializers.CharField(max_length=255)
    )
    water = serializers.IntegerField()
    typeoftea = serializers.CharField()
