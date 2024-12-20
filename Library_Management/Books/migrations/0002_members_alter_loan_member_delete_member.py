# Generated by Django 5.1.4 on 2024-12-09 12:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField(blank=True, null=True)),
                ('membership_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='loan',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.members'),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
