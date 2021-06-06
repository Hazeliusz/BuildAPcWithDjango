from rest_framework import serializers
from .models import *

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'

class GpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gpu
        fields = '__all__'

class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'

class PsuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psu
        fields = '__all__'

class SsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ssd
        fields = '__all__'