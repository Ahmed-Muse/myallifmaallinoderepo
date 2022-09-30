# Generated by Django 3.2.8 on 2022-09-28 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allifmaalapp', '0002_allifmaalinvoiceitemsmodel_allifmaalinvoicesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllifmaalCustomerPaymentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('comments', models.CharField(blank=True, default='comment', max_length=15, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='allifcustpaymentreltedname', to='allifmaalapp.allifmaalcustomersmodel')),
            ],
        ),
    ]