# Generated by Django 4.2.2 on 2023-09-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_user_created_time_user_updated_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer', models.ImageField(default='None', upload_to='img')),
                ('flat', models.ImageField(default='None', upload_to='img')),
                ('investment', models.ImageField(default='None', upload_to='img')),
                ('insurance', models.ImageField(default='None', upload_to='img')),
            ],
        ),
    ]
