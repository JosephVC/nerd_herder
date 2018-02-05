# Generated by Django 2.0.1 on 2018-02-05 08:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('date_scheduled', models.DateTimeField(blank=True, null=True)),
                ('rsvp_max', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('value', models.FloatField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.CompanyContact')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='TalkInvitation',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('invited_on', models.DateTimeField(auto_now_add=True)),
                ('accepted_on', models.DateTimeField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('talk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speakers.Talk')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VenueSponsorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('sponsor_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='venue_sponsorships', to='companies.CompanyContact')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Venue')),
                ('venue_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='venue_contacts', to='companies.CompanyContact')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='talks',
            field=models.ManyToManyField(through='events.TalkInvitation', to='speakers.Talk'),
        ),
    ]
