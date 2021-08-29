# Generated by Django 3.2.5 on 2021-08-25 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_productcategory_number_of_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopByDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='productcategory',
            name='shopbydepartment',
            field=models.ManyToManyField(to='app.ShopByDepartment'),
        ),
    ]
