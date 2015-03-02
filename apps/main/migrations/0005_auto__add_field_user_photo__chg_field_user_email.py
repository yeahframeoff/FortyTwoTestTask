# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.photo'
        db.add_column('main_user', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)


        # Changing field 'User.email'
        db.alter_column('main_user', 'email', self.gf('django.db.models.fields.EmailField')(max_length=64))

    def backwards(self, orm):
        # Deleting field 'User.photo'
        db.delete_column('main_user', 'photo')


        # Changing field 'User.email'
        db.alter_column('main_user', 'email', self.gf('django.db.models.fields.CharField')(max_length=64))

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
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '64'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'})
        }
    }

    complete_apps = ['main']