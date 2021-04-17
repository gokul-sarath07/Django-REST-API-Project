from django import forms
from .models import RoomRecordInput, AgeRecordInput


class RoomFormData(forms.ModelForm):
    """
    ModelForm which connects the RoomRecordInput table to the form.
    """
    class Meta:
        model = RoomRecordInput
        fields = '__all__'


class AgeFormData(forms.ModelForm):
    """
    ModelForm which connects the AgeRecordInput table to the form.
    """
    class Meta:
        model = AgeRecordInput
        fields = '__all__'
