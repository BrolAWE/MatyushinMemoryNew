# Generated by Django 4.1.3 on 2022-12-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_imgsample_member_experiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgsample',
            name='zv',
            field=models.CharField(blank=True, choices=[('Ц', 'Ц'), ('Б', 'Б')], max_length=50, null=True),
        ),
    ]
