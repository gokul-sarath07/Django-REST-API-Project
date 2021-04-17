from rest_framework import serializers
from .models import RoomRecordInput, RoomRecordOutput, AgeRecordInput, AgeRecordOutput


class RoomRecordInputSerializer(serializers.ModelSerializer):
    invalid_trigger = serializers.SerializerMethodField('get_invalid_trigger')
    key = serializers.SerializerMethodField('get_key')
    name = serializers.SerializerMethodField('get_name')
    reuse = serializers.SerializerMethodField('get_reuse')
    support_multiple = serializers.SerializerMethodField('get_support_multiple')
    supported_values = serializers.SerializerMethodField('get_supported_values')
    type = serializers.SerializerMethodField('get_type')
    validation_parser = serializers.SerializerMethodField('get_validation_parser')
    values = serializers.SerializerMethodField('get_values')

    class Meta:
        model = RoomRecordInput
        fields = ('invalid_trigger', 'key', 'name', 'reuse',
                  'support_multiple', 'pick_first', 'supported_values', 'type',
                  'validation_parser', 'values')

    def get_invalid_trigger(self, roomRecordObj):
        return "invalid_ids_stated"

    def get_key(self, roomRecordObj):
        return "ids_stated"

    def get_name(self, roomRecordObj):
        return "govt_id"

    def get_reuse(self, roomRecordObj):
        return True

    def get_support_multiple(self, roomRecordObj):
        support_multiple = False
        if len(roomRecordObj.value) > 1:
            support_multiple = True
        return support_multiple

    def get_supported_values(self, roomRecordObj):
        supported_values = ["pan", "aadhaar", "college", "corporate",
                            "dl", "voter", "passport", "local"]
        return supported_values

    def get_type(self, roomRecordObj):
        type = ["id"]
        return type

    def get_validation_parser(self, roomRecordObj):
        return "finite_values_entity"

    def get_values(self, roomRecordObj):
        values = []
        for val in roomRecordObj.value:
            values.append({"entity_type": "id", "value": val})
        return values

class RoomRecordOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomRecordOutput
        fields = ('filled', 'partially_filled', 'trigger', 'parameters')

# =================================== API 2 ====================================

class AgeRecordInputSerializer(serializers.ModelSerializer):

    invalid_trigger = serializers.SerializerMethodField('get_invalid_trigger')
    key = serializers.SerializerMethodField('get_key')
    name = serializers.SerializerMethodField('get_name')
    reuse = serializers.SerializerMethodField('get_reuse')
    type = serializers.SerializerMethodField('get_type')
    validation_parser = serializers.SerializerMethodField('get_validation_parser')
    support_multiple = serializers.SerializerMethodField('get_support_multiple')
    constraint = serializers.SerializerMethodField('get_constraint')
    var_name = serializers.SerializerMethodField('get_var_name')
    values = serializers.SerializerMethodField('get_values')

    class Meta:
        model = AgeRecordInput
        fields = ('invalid_trigger', 'key', 'name', 'reuse',
                  'support_multiple', 'pick_first', 'type',
                  'validation_parser', 'constraint', 'var_name', 'values')

    def get_invalid_trigger(self, ageRecordObj):
        return "invalid_age"

    def get_key(self, ageRecordObj):
        return "age_stated"

    def get_name(self, ageRecordObj):
        return "age"

    def get_reuse(self, ageRecordObj):
        return True

    def get_type(self, ageRecordObj):
        type = ["number"]
        return type

    def get_support_multiple(self, ageRecordObj):
        support_multiple = False
        if len(ageRecordObj.value) > 1:
            support_multiple = True
        return support_multiple

    def get_validation_parser(self, ageRecordObj):
        return "numeric_values_entity"

    def get_constraint(self, ageRecordObj):
        return "x>=18 and x<=30" if ageRecordObj.constraint_value else None

    def get_var_name(self, ageRecordObj):
        return "x" if ageRecordObj.constraint_value else None

    def get_values(self, ageRecordObj):
        values = []
        for val in ageRecordObj.value:
            values.append({"entity_type": "number", "value": val})
        return values

class AgeRecordOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRecordOutput
        fields = ('filled', 'partially_filled', 'trigger', 'parameters')
