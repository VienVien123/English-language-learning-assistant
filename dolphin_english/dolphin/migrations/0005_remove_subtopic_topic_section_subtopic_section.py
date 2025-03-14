# Generated by Django 5.1.6 on 2025-03-11 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dolphin', '0004_subtopic_num_part'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtopic',
            name='topic',
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField(default=1)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='dolphin.topic')),
            ],
        ),
        migrations.AddField(
            model_name='subtopic',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtopics', to='dolphin.section'),
        ),
    ]
