from . models import City, District, Street, House, Entrance
from rest_framework import serializers
from django.utils.datastructures import  MultiValueDict
class ModelSerializerId(serializers.ModelSerializer):
    def to_internal_value(self, data):
        if data:
            if isinstance(data,int):
                return self.Meta.model.objects.get(id=data)
            elif isinstance(data,str):
                try:
                    return self.Meta.model.objects.get(id=int(data))
                except:
                    pass
          #  elif isinstance(data,MultiValueDict):
          #      ls = [ int(v) for k,v in data.items() ]
          #      return self.Meta.model.objects.filter(id__in=ls)
            else:
                return self.Meta.model.objects.get(id=int(data['id']))
        return None

class EntranceInlineSerializer(ModelSerializerId):
    class Meta:
        model = Entrance
        exclude = ('house',)
class HouseInlineSerializer(ModelSerializerId):
    nodes = EntranceInlineSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = House
        exclude = ('street',)
        depth = 1
class StreetInlineSerializer(ModelSerializerId):
    nodes = HouseInlineSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Street
        exclude = ('district',)
        depth = 1
class DistrictInlineSerializer(ModelSerializerId):
    nodes = StreetInlineSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = District
        exclude = ('city',)
        depth = 1

class CityInlineSerializer(ModelSerializerId):
    class Meta:
        model = City
        fields = '__all__'
class CitySerializer(serializers.ModelSerializer):
    nodes = DistrictInlineSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = City
        fields = '__all__'
        depth = 1
class DistrictSerializer(serializers.ModelSerializer):
    nodes = StreetInlineSerializer(many=True, required=False, read_only=True)
    city = CityInlineSerializer()
    class Meta:
        model = District
        fields = '__all__'
        depth = 1
class StreetSerializer(serializers.ModelSerializer):
    nodes = HouseInlineSerializer(many=True, required=False, read_only=True)
    district = DistrictInlineSerializer()
    class Meta:
        model = Street
        fields = '__all__'
        depth = 1
class HouseSerializer(serializers.ModelSerializer):
    nodes = EntranceInlineSerializer(many=True, required=False, read_only=True)
    street = StreetInlineSerializer()
    class Meta:
        model = House
        fields = '__all__'
        depth = 1
class EntranceSerializer(serializers.ModelSerializer):
    house = HouseInlineSerializer()
    class Meta:
        model = Entrance
        fields = '__all__'
        depth = 1
