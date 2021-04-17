from django import forms
from .models import RoomRecordInput, AgeRecordInput


class RoomFormData(forms.ModelForm):
    class Meta:
        model = RoomRecordInput
        fields = '__all__'

class AgeFormData(forms.ModelForm):
    class Meta:
        model = AgeRecordInput
        fields = '__all__'
