from rest_framework import serializers
from .models import MakeTea, Add
from HowToMakeTea.api.tea.TeaMachine import Tea_Machine


class PrepareTea(serializers.ModelSerializer):
    class Meta:
        model = MakeTea
        fields = "__all__"


class PrepareAdd(serializers.ModelSerializer):
    class Meta:
        model = Add
        fields = "__all__"
