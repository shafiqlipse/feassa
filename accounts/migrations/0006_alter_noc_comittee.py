# Generated by Django 5.0.7 on 2024-08-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_noc_comittee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noc',
            name='comittee',
            field=models.CharField(choices=[('Technical ', 'Technical '), ('Welfare ', 'Welfare '), ('Protocol', 'Protocol'), ('Finance', 'Finance'), ('Competitions', 'Competitions'), ('Medical /Health', 'Medical /Health'), ('Security and Safety', 'Security and Safety'), ('Transport', 'Transport'), ('Corporate Relations', 'Corporate Relations'), ('Media', 'Media'), ('Secretariat', 'Secretariat'), ('Sports coordinators', 'Sports coordinators'), ('Refeere', 'Refeere'), ('Umpires', 'Umpires'), ('Matron', 'Matron'), ('Patron', 'Patron'), ('OR-TAMISEM Sports  coordinator', 'OR-TAMISEM Sports  coordinator'), ('MOSCASMoEST', 'MOSCASMoEST'), ('MoEST', 'MoEST'), ('UMISSETA/UMITASHUMTA chairperson', 'UMISSETA/UMITASHUMTA chairperson'), ('UMISSETA/UMITASHUMTA vice chairperson', 'UMISSETA/UMITASHUMTA vice chairperson'), ('UMISSETA secretary', 'UMISSETA secretary'), ('UMISSETA Treasury.', 'UMISSETA Treasury.')], max_length=50),
        ),
    ]
