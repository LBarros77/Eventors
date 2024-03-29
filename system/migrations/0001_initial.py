# Generated by Django 2.2.1 on 2023-02-28 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(max_length=140)),
                ('corporate_name', models.CharField(max_length=140)),
                ('fantasy_name', models.CharField(blank=True, max_length=140, null=True)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('position', models.CharField(max_length=20)),
                ('cep', models.CharField(blank=True, max_length=17, null=True)),
                ('public_place', models.CharField(blank=True, max_length=249, null=True)),
                ('complement', models.CharField(blank=True, max_length=249, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=80, null=True)),
                ('city', models.CharField(blank=True, max_length=80, null=True)),
                ('state', models.CharField(blank=True, max_length=80, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=17, null=True)),
                ('segmentation', models.CharField(choices=[('0', 'Sem Segmento'), ('1', 'Informática'), ('2', 'Eletro'), ('3', 'Materiais de Construção'), ('4', 'Veterinário'), ('5', 'Varejo Alimentar'), ('6', 'Farma')], default='0', max_length=3)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cep', models.CharField(max_length=17)),
                ('public_place', models.CharField(max_length=249)),
                ('complement', models.CharField(blank=True, max_length=249, null=True)),
                ('neighborhood', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('number', models.IntegerField()),
                ('first_date', models.DateField()),
                ('first_hour', models.TimeField()),
                ('last_date', models.DateField()),
                ('last_hour', models.TimeField()),
                ('qtd_registration', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('name_cracha', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('0', 'Visitente'), ('1', 'Expositor'), ('2', 'Apoio')], default='0', max_length=3)),
                ('cell_phone', models.CharField(max_length=17)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=17)),
                ('role', models.CharField(max_length=50)),
                ('opt_in', models.CharField(choices=[('0', 'Sim'), ('1', 'Não')], max_length=3)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.Company')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.Event')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Person')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RafflePrizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Event')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Person')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('question', models.TextField(max_length=100)),
                ('approve', models.BooleanField(default=False)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.Event')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.Event')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Person')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Register')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
