# Generated by Django 2.2 on 2019-04-16 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('profession', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('hero', 'Hero'), ('villain', 'Villain'), ('sidekick', 'Sidekick'), ('comedic', 'Comedic'), ('extra', 'Extra'), ('solo', 'Solo Artist')], default='extra', max_length=20)),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='proteges', to='characters.Character')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='characters.Team')),
            ],
        ),
        migrations.CreateModel(
            name='LineModifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifier', models.CharField(max_length=50)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='line_modifiers', to='characters.Character')),
            ],
        ),
    ]