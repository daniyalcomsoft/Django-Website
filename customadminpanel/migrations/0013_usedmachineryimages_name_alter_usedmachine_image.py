# Generated by Django 4.1.7 on 2023-09-25 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customadminpanel', '0012_usedmachineryimages_usedmachine'),
    ]

    operations = [
        migrations.AddField(
            model_name='usedmachineryimages',
            name='Name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customadminpanel.usedmachine', verbose_name='Machine Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usedmachine',
            name='Image',
            field=models.ImageField(null=True, upload_to='media/product'),
        ),
    ]