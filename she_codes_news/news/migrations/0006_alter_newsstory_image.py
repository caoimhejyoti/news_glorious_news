# Generated by Django 4.2.2 on 2023-12-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_newsstory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
