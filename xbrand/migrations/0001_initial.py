# Generated by Django 2.2.3 on 2019-07-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('tesis', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(help_text='Banner image', upload_to='banner/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='WomenProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('image_1', models.ImageField(help_text='Women product image', upload_to='women_product')),
                ('image_2', models.ImageField(blank=True, help_text='Women product image', upload_to='women_product')),
                ('image_3', models.ImageField(blank=True, help_text='Women product image', upload_to='women_product')),
                ('image_4', models.ImageField(blank=True, help_text='Women product image', upload_to='women_product')),
                ('image_5', models.ImageField(blank=True, help_text='Women product image', upload_to='women_product')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('new', models.BooleanField(default=True)),
                ('kind', models.CharField(default='jacket, pants, t-short, sweatshirt, dress, shoes', max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
