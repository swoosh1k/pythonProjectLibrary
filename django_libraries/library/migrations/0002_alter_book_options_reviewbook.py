# Generated by Django 4.2.7 on 2023-11-19 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.CreateModel(
            name='ReviewBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='комментарий')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Книжка',
                'verbose_name_plural': 'книги',
            },
        ),
    ]
