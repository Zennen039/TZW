# Generated by Django 5.1.6 on 2025-02-26 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tzwapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='users/%Y/%m'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('subject', 'category')},
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('subject', 'course')},
        ),
    ]
