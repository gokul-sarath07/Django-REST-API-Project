from django.shortcuts import render
from .forms import RoomFormData, AgeFormData
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RoomRecordInput, RoomRecordOutput, AgeRecordInput, AgeRecordOutput
from .models import validate_finite_values_entity, validate_numeric_entity
from .serializers import RoomRecordInputSerializer, RoomRecordOutputSerializer
from .serializers import AgeRecordInputSerializer, AgeRecordOutputSerializer


def home_view(request):
    """
    Display the home page.
    """
    return render(request, "myAppOne/index.html")


def room_form_view(request):
    """
    Display API 1's input form page, accept and store the input data and
    pass input data for validation.
    """
    context = {}
    context['form'] = RoomFormData()
    if request.method == 'POST':
        form = RoomFormData(request.POST)
        try:
            if form.is_valid():
                form.save(commit=True)
                record = RoomRecordInput.objects.filter(id=form.cleaned_data['id'])
                serializer = RoomRecordInputSerializer(record, many=True).data
                save_room_validated_values(serializer[0])
        except Exception as e:
            print("[EXCEPTION] ", e)
    return render(request, "myAppOne/room_form_page.html", context)


def save_room_validated_values(serializer):
    """
    Pass the input values for validating based in conditions.
    """
    values = serializer["values"]
    pick_first = serializer["pick_first"]
    supported_values = serializer["supported_values"]
    invalid_trigger = serializer["invalid_trigger"]
    key = serializer["key"]
    support_multiple = serializer["support_multiple"]
    validate_finite_values_entity(values, supported_values, invalid_trigger,
                                    key, support_multiple, pick_first)


class RoomRecordAPIView(APIView):
    """
    Display the output of API 1 in APIView
    """
    def get(self, request):
        record = RoomRecordOutput.objects.all()
        serializer = RoomRecordOutputSerializer(record, many=True)
        return Response(serializer.data)


# ==================================== API 2 ===================================

def age_form_view(request):
    """
    Display API 2's input form page, accept and store the input data and
    pass input data for validation.
    """
    context = {}
    context['form'] = AgeFormData()
    if request.method == 'POST':
        form = AgeFormData(request.POST)
        try:
            if form.is_valid():
                form.save(commit=True)
                record = AgeRecordInput.objects.filter(id=form.cleaned_data['id'])
                serializer = AgeRecordInputSerializer(record, many=True).data
                save_age_validated_values(serializer[0])
        except Exception as e:
            print("[EXCEPTION] ", e)
    return render(request, "myAppOne/age_form_page.html", context)


def save_age_validated_values(serializer):
    """
    Pass the input values for validating based in conditions.
    """
    pick_first = serializer["pick_first"]
    support_multiple = serializer["support_multiple"]
    values = serializer["values"]
    invalid_trigger = serializer["invalid_trigger"]
    key = serializer["key"]
    constraint = serializer["constraint"]
    var_name = serializer["var_name"]
    validate_numeric_entity(values, invalid_trigger, key, support_multiple,
                            pick_first, constraint, var_name)


class AgeRecordAPIView(APIView):
    """
    Display the output of API 2 in APIView
    """
    def get(self, request):
        record = AgeRecordOutput.objects.all()
        serializer = AgeRecordOutputSerializer(record, many=True)
        return Response(serializer.data)
