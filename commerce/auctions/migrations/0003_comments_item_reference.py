# Generated by Django 3.2.8 on 2021-10-19 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20211018_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='item_reference',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_comment', to='auctions.items'),
        ),
    ]
