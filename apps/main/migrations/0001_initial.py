# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('main_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['User'])

        # Adding model 'Contact'
        db.create_table('main_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User'])),
            ('contact_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('main', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('main_user')

        # Deleting model 'Contact'
        db.delete_table('main_contact')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['main']