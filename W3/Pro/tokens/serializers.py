
from rest_framework import serializers
from tokens.models import Register

class RegisterSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'name', 'email', 'address']

        

        

    
    