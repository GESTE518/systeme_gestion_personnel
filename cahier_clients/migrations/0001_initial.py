# Generated by Django 4.2.19 on 2025-02-11 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cahier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employes.employe', verbose_name='Employé')),
            ],
        ),
        migrations.CreateModel(
            name='EchangeBiens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_bien', models.CharField(max_length=200)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('statut', models.CharField(max_length=50)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/echanges/')),
                ('cahier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cahier_clients.cahier')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employes.employe')),
            ],
        ),
        migrations.CreateModel(
            name='AvanceArgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('statut', models.CharField(max_length=50)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/avances/')),
                ('cahier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cahier_clients.cahier')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employes.employe')),
            ],
        ),
    ]
