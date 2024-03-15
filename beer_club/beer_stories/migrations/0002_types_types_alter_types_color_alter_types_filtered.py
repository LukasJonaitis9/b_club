# Generated by Django 5.0 on 2024-03-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer_stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='types',
            name='types',
            field=models.CharField(blank=True, choices=[('w', 'Wheat beer'), ('l', 'Lager'), ('p', 'Pilsner'), ('i', 'IPA'), ('a', 'ALE'), ('s', 'Stout'), ('b', 'Bock')], help_text='Chose your type of beer!', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='types',
            name='color',
            field=models.CharField(choices=[('l', 'Light / Straw'), ('a', 'Amber'), ('c', 'Copper / Reddish-Brown'), ('b', 'Brown'), ('d', 'Black')], help_text='Choose your colour of beer!', max_length=1),
        ),
        migrations.AlterField(
            model_name='types',
            name='filtered',
            field=models.CharField(blank=True, choices=[('y', 'Filtered'), ('n', 'Unfiltered')], help_text='Choose filtered or unfiltered beer!', max_length=1, null=True),
        ),
    ]
