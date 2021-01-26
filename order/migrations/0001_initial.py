# Generated by Django 3.1.5 on 2021-01-26 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goodies', '0006_product_last_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.PositiveIntegerField()),
                ('dateordered', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodies.product')),
            ],
        ),
    ]