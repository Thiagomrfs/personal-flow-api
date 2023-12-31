# Generated by Django 4.2.2 on 2023-06-20 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=50)),
                ('criador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projetos_criados', to=settings.AUTH_USER_MODEL)),
                ('participantes', models.ManyToManyField(related_name='projetos_colaborados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
