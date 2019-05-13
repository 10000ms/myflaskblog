# Generated by Django 2.2 on 2019-05-10 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.middleware.current_user


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190507_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='creator',
            field=models.ForeignKey(blank=True, default=main.middleware.current_user.get_current_user, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='father_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Blog'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(blank=True, default=main.middleware.current_user.get_current_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]