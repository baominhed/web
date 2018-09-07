# Generated by Django 2.1 on 2018-08-23 16:26

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0106_auto_20180823_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='BountyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('status', models.CharField(choices=[('o', 'open'), ('c', 'closed'), ('f', 'funded')], db_index=True, default='o', max_length=1)),
                ('github_url', models.CharField(default='', max_length=255)),
                ('eth_address', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField(default='', max_length=500)),
                ('comment_admin', models.TextField(blank=True, max_length=500)),
                ('amount', models.FloatField(default=0.0)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bounty_requests', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
