# Generated by Django 2.1.4 on 2019-02-16 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190216_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='coinbase_id',
            field=models.CharField(default='sdfds', max_length=60),
            preserve_default=False,
        ),
    ]
