# Generated by Django 5.2.4 on 2025-07-23 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_moral', models.CharField(blank=True, max_length=255)),
                ('bad_moral', models.CharField(blank=True, max_length=255)),
                ('story_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
