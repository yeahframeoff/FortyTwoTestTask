# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


class Migration(DataMigration):

    def forwards(self, orm):
        """
        Populates models main.User and main.Contact with data necessary for mainpage.
        """
        from django.core.management import call_command
        from os.path import join as joinpath
        from django.conf import settings
        call_command('loaddata', joinpath(
            settings.APP_MAIN_DIR, 'fixtures/initial_data.json'))

    def backwards(self, orm):
        """
        Nothing happens backwards.
        """
        pass

    models = {
        'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.User']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'main.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'})
        }
    }

    complete_apps = ['main']
    symmetrical = True
    no_dry_run = False
