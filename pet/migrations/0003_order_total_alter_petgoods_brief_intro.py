# Generated by Django 4.1.7 on 2023-06-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_petgoods_goods_status_alter_adoptpet_apply_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=1, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='petgoods',
            name='brief_intro',
            field=models.TextField(verbose_name='商品简介'),
        ),
    ]
