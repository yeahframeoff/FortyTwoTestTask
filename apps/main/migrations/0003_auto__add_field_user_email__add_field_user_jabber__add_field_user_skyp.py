# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.email'
        db.add_column('main_user', 'email',
                      self.gf('django.db.models.fields.CharField')(max_length=64, default=''),
                      keep_default=False)

        # Adding field 'User.jabber'
        db.add_column('main_user', 'jabber',
                      self.gf('django.db.models.fields.CharField')(max_length=64, default=''),
                      keep_default=False)

        # Adding field 'User.skype'
        db.add_column('main_user', 'skype',
                      self.gf('django.db.models.fields.CharField')(max_length=64, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.email'
        db.delete_column('main_user', 'email')

        # Deleting field 'User.jabber'
        db.delete_column('main_user', 'jabber')

        # Deleting field 'User.skype'
        db.delete_column('main_user', 'skype')


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
            'email': ('django.db.models.fields.CharField', [], {'max_length': '64', 'default': "''"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '64', 'default': "''"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'default': "''"}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '64', 'default': "''"})
        }
    }

    complete_apps = ['main']