# Generated by Django 4.2.7 on 2023-12-02 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_profile_rename_text_post_body_alter_post_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='text',
        ),
    ]
