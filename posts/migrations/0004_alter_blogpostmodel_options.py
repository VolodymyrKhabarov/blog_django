# Generated by Django 4.1.5 on 2023-02-05 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_blogpostcategorymodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpostmodel',
            options={'ordering': ('updated_at',), 'verbose_name': 'blogpost', 'verbose_name_plural': 'blogposts'},
        ),
    ]
