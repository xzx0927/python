# Generated by Django 3.2.8 on 2023-12-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='upload/covers/abc.png', upload_to='upload/covers', verbose_name='封面'),
        ),
    ]
