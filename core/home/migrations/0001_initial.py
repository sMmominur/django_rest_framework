# Generated by Django 5.0.6 on 2024-05-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EiinTbl',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('eiin', models.CharField(max_length=15)),
                ('code', models.CharField(blank=True, max_length=15, null=True)),
                ('name', models.CharField(max_length=255)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('upazila', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'eiin_tbl',
                'ordering': ['id'],
                'indexes': [models.Index(fields=['eiin'], name='eiin_tbl_eiin_94fedc_idx'), models.Index(fields=['code'], name='eiin_tbl_code_c057fd_idx'), models.Index(fields=['name'], name='eiin_tbl_name_f0c433_idx')],
            },
        ),
    ]
