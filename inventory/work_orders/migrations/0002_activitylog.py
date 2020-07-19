# Generated by Django 3.0.5 on 2020-07-11 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work_orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=50)),
                ('increment', models.BooleanField(default=False)),
                ('quantityrequired', models.IntegerField(max_length=6)),
                ('quantitycompleted', models.IntegerField(max_length=6)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('jobid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work_orders.Jobs')),
                ('partsrequired', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parts.PartsList')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]