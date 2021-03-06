# Generated by Django 3.2.8 on 2021-10-30 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_comments_item_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='offer',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='comments',
            name='item_reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_comment', to='auctions.items'),
        ),
    ]
