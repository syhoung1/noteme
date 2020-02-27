# Generated by Django 3.0.3 on 2020-02-27 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200226_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.IntegerField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]