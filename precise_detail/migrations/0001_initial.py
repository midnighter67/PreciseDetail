# Generated by Django 5.1 on 2024-09-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=50)),
                ('last', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=20)),
                ('bed', models.IntegerField(null=True)),
                ('bath', models.IntegerField(null=True)),
                ('sqft', models.IntegerField(null=True)),
                ('pets', models.IntegerField(null=True)),
                ('frequency', models.IntegerField(null=True)),
            ],
        ),
    ]
