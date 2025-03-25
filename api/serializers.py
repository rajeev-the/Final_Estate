# serializers.py
from rest_framework import serializers
from .models import Agent, Property, GeneralData,UserData

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class GeneralDataSerializer(serializers.ModelSerializer):
    top_rate = PropertySerializer(many=True, read_only=True)
    featured = PropertySerializer(many=True, read_only=True)
    recommendation = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = GeneralData
        fields = '__all__'



class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'  # Include all fields (phone, name)