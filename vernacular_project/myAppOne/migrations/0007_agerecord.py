# Generated by Django 3.2 on 2021-04-16 12:44

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myAppOne', '0006_alter_roomrecordoutput_trigger'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRecord',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('value', multiselectfield.db.fields.MultiSelectField(choices=[(20, 20), (29, 29), (33, 33), (2, 2), (34, 34), (11, 11), (30, 30), (-1, -1), (7, 7), (16, 16), (25, 25), (26, 26), (35, 35), (3, 3), (12, 12), (21, 21), (22, 22), (31, 31), (8, 8), (17, 17), (27, 27), (13, 13), (32, 32), (18, 18), (4, 4), (5, 5), (14, 14), (23, 23), (9, 9), (1, 1), (24, 24), (10, 10), (19, 19), (28, 28), (6, 6), (15, 15)], default=list, max_length=98)),
            ],
        ),
    ]
