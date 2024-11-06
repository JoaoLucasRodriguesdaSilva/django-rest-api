# Generated by Django 5.1.2 on 2024-11-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('seconds', models.IntegerField()),
            ],
            options={
                'db_table': 'music',
            },
        ),
    ]
