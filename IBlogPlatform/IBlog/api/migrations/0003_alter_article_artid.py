# Generated by Django 5.2 on 2025-05-08 23:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_author_groups_author_is_active_author_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='artID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
