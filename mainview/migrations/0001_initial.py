# Generated by Django 2.2.2 on 2019-07-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('item_title', models.CharField(max_length=30)),
                ('item_description', models.TextField()),
                ('item_image', models.ImageField(blank=True, upload_to='media')),
                ('item_price', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('item_category', models.CharField(default='cutlery', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('itemjson', models.CharField(blank=True, max_length=5200)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('sub', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
            ],
        ),
    ]
