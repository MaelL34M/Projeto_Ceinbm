# Generated by Django 4.1.4 on 2023-02-12 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_alter_planejamentoanual_docente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planodeaula',
            name='docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plano_aula', to='principal.docente', verbose_name='Docente'),
        ),
    ]
