# Generated by Django 3.0.8 on 2020-07-25 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='application',
            name='info',
        ),
        migrations.AlterField(
            model_name='application',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Candidate'),
        ),
    ]