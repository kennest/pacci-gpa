# Generated by Django 4.1.1 on 2022-09-13 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpa_back', '0003_historicalintervention_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluserprofil',
            name='role',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gpa_back.userrole', verbose_name="Role de l'utilisateur"),
        ),
        migrations.AlterField(
            model_name='userprofil',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpa_back.userrole', verbose_name="Role de l'utilisateur"),
        ),
    ]