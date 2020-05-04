# Generated by Django 3.0.5 on 2020-04-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='partslist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partnumber', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=20)),
                ('supplier', models.CharField(max_length=50)),
                ('stockonhand', models.IntegerField(blank=True)),
                ('minimumstock', models.IntegerField(blank=True)),
                ('reorderqtys', models.IntegerField(blank=True)),
                ('qtyperassembly', models.IntegerField(blank=True)),
                ('boxsize', models.IntegerField(blank=True)),
                ('leadtime', models.CharField(max_length=50)),
                ('weight', models.IntegerField(blank=True)),
            ],
        ),
    ]