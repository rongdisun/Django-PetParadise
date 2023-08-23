# Generated by Django 4.1.7 on 2023-06-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petgoods',
            name='goods_status',
            field=models.SmallIntegerField(choices=[(0, '下架'), (1, '在售')], default=1, verbose_name='上架状态'),
        ),
        migrations.AlterField(
            model_name='adoptpet',
            name='apply_status',
            field=models.SmallIntegerField(choices=[(0, '拒绝'), (1, '通过'), (2, '待审核')], default=2, verbose_name='审核状态'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='adopt_status',
            field=models.SmallIntegerField(choices=[(0, '未被领养'), (1, '已被领养')], default=0, verbose_name='领养状态'),
        ),
    ]
