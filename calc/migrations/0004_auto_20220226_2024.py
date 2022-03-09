# Generated by Django 3.2 on 2022-02-26 14:54

import calc.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_alter_profile_calculator_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calculatormaster',
            options={'verbose_name_plural': '   Calculator Master'},
        ),
        migrations.AlterModelOptions(
            name='currencymaster',
            options={'verbose_name_plural': '     Currency Master'},
        ),
        migrations.AlterModelOptions(
            name='currencyratemaster',
            options={'ordering': ['-effective_date', 'name'], 'verbose_name_plural': '    Currency Rate Master'},
        ),
        migrations.AlterModelOptions(
            name='journalmaster',
            options={'verbose_name_plural': '  Journal Master'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': '      Profile'},
        ),
        migrations.RemoveField(
            model_name='journalmaster',
            name='calc_ids',
        ),
        migrations.AddField(
            model_name='journalmaster',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='journalmaster',
            name='calculator_ids',
            field=models.ManyToManyField(to='calc.CalculatorMaster', verbose_name='Reference Calculator'),
        ),
        migrations.AddField(
            model_name='journalmaster',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journalmaster',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='calculatormaster',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='calculatormaster',
            name='currency_ids',
            field=models.ManyToManyField(to='calc.CurrencyMaster', verbose_name='Secondary Currency'),
        ),
        migrations.AlterField(
            model_name='calculatormaster',
            name='directory_name',
            field=models.CharField(editable=False, max_length=100, unique=True, verbose_name='Directory'),
        ),
        migrations.AlterField(
            model_name='calculatormaster',
            name='is_published',
            field=models.BooleanField(verbose_name='Is Published'),
        ),
        migrations.AlterField(
            model_name='calculatormaster',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='calculatormaster',
            name='primary_currency_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_currency_id', to='calc.currencymaster', verbose_name='Primary Currency'),
        ),
        migrations.AlterField(
            model_name='currencymaster',
            name='code',
            field=models.CharField(blank=True, help_text='Currency Code', max_length=10, unique=True, verbose_name='Currency Code'),
        ),
        migrations.AlterField(
            model_name='currencymaster',
            name='name',
            field=models.CharField(blank=True, help_text='Currency Name', max_length=100, unique=True, verbose_name='Currency Name'),
        ),
        migrations.AlterField(
            model_name='currencyratemaster',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='currencyratemaster',
            name='code',
            field=models.CharField(blank=True, help_text='Conversion Code', max_length=10, unique=True, verbose_name='Conversion Code'),
        ),
        migrations.AlterField(
            model_name='currencyratemaster',
            name='conversion_rate',
            field=models.FloatField(verbose_name='Conversion Rate'),
        ),
        migrations.AlterField(
            model_name='currencyratemaster',
            name='effective_date',
            field=models.DateField(verbose_name='Effective Date'),
        ),
        migrations.AlterField(
            model_name='currencyratemaster',
            name='from_currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_currency', to='calc.currencymaster', verbose_name='From Currency'),
        ),
        migrations.AlterField(
            model_name='currencyratemaster',
            name='name',
            field=models.CharField(blank=True, help_text='Conversion Name', max_length=100, unique=True, verbose_name='Conversion Name'),
        ),
        migrations.AlterField(
            model_name='currencyratemaster',
            name='to_currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_currency', to='calc.currencymaster', verbose_name='To Currency'),
        ),
        migrations.AlterField(
            model_name='journalmaster',
            name='code',
            field=models.CharField(max_length=10, unique=True, verbose_name='Journal Code'),
        ),
        migrations.AlterField(
            model_name='journalmaster',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Journal Name'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded at')),
                ('document', models.FileField(upload_to=calc.models.get_upload_to, verbose_name='Document')),
                ('calculator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calc_id', to='calc.calculatormaster', verbose_name='Calculator')),
            ],
            options={
                'verbose_name_plural': ' Document',
                'db_table': 'document_master',
            },
        ),
    ]