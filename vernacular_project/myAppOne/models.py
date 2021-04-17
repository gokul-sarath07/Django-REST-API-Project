from django.db import models
from multiselectfield import MultiSelectField
from typing import List, Dict, Callable, Tuple

# API 1

OPTIONS = ( ("pan", "Pan"),
            ("aadhaar", "Aadhaar"),
            ("college", "College"),
            ("corporate", "Corporate"),
            ("dl", "DL"),
            ("voter", "Voter"),
            ("passport", "Passport"),
            ("local", "Local"),
            ("other", "Other") )

# Create your models here.
class RoomRecordInput(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    value = MultiSelectField(choices=OPTIONS, default=list)
    pick_first = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class RoomRecordOutput(models.Model):
    filled = models.BooleanField()
    partially_filled = models.BooleanField()
    trigger = models.CharField(max_length=20, blank=True)
    parameters = models.TextField()

SlotValidationResult = Tuple[bool, bool, str, Dict]
def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None,
                                invalid_trigger: str = None, key: str = None,
                                support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:

                                filled = True
                                partially_filled = False
                                trigger = ''
                                parameters = {}

                                for value in values:
                                    if value["value"] not in supported_values:
                                        filled = False
                                        partially_filled = True
                                        trigger = invalid_trigger
                                        parameters = {}
                                        break
                                    if pick_first:
                                        if len(parameters) == 0:
                                            parameters[key] = value["value"]
                                        else:
                                            continue
                                    else:
                                        if len(parameters) == 0:
                                            parameters[key] = [value["value"]]
                                        elif support_multiple:
                                            parameters[key].append(value["value"])

                                new_instance = RoomRecordOutput.objects.create(filled = filled,
                                                    partially_filled = partially_filled,
                                                    trigger = trigger,
                                                    parameters = parameters)

# ==================================== API 2 ===================================

AGES = list(((val, val) for val in range(-1, 36) if val not in [num for num in range(0, 15)]))

class AgeRecordInput(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    value = MultiSelectField(choices=AGES, default=list)
    pick_first = models.BooleanField(default=False)
    constraint_value = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class AgeRecordOutput(models.Model):
    filled = models.BooleanField()
    partially_filled = models.BooleanField()
    trigger = models.CharField(max_length=20, blank=True)
    parameters = models.TextField()

def validate_numeric_entity(values: List[Dict], invalid_trigger: str = None, key: str = None,
                            support_multiple: bool = True, pick_first: bool = False, constraint=None,
                            var_name=None, **kwargs) -> SlotValidationResult:

                            filled = True
                            partially_filled = False
                            trigger = ''
                            parameters = {}

                            for value in values:
                                number = int(value["value"])
                                if constraint == None:
                                    add_parameter_values(number, pick_first, parameters, support_multiple, key)
                                elif type(constraint) == str:
                                    if number >= 18 and number <= 30:
                                        add_parameter_values(number, pick_first, parameters, support_multiple, key)
                                    else:
                                        partially_filled = True
                                        filled = False
                                        trigger = invalid_trigger

                            new_instance = AgeRecordOutput.objects.create(filled = filled,
                                                partially_filled = partially_filled,
                                                trigger = trigger,
                                                parameters = parameters)

def add_parameter_values(number, pick_first, parameters, support_multiple, key):
        if (pick_first and not support_multiple) or (pick_first and support_multiple):
            if len(parameters) == 0:
                parameters[key] = number
        elif (not pick_first and support_multiple) or (not pick_first and not support_multiple):
            if len(parameters) == 0:
                parameters[key] = [number]
            else:
                parameters[key].append(number)
