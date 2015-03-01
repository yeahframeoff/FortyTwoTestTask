# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.name'
        db.delete_column('main_user', 'name')

        # Deleting field 'User.surname'
        db.delete_column('main_user', 'surname')

        # Adding field 'User.first_name'
        db.add_column('main_user', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='First name', max_length=32),
                      keep_default=False)

        # Adding field 'User.last_name'
        db.add_column('main_user', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='Last name', max_length=32),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'User.name'
        db.add_column('main_user', 'name',
                      self.gf('django.db.models.fields.CharField')(default='First name', max_length=32),
                      keep_default=False)

        # Adding field 'User.surname'
        db.add_column('main_user', 'surname',
                      self.gf('django.db.models.fields.CharField')(default='Last name', max_length=32),
                      keep_default=False)

        # Deleting field 'User.first_name'
        db.delete_column('main_user', 'first_name')

        # Deleting field 'User.last_name'
        db.delete_column('main_user', 'last_name')


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
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['main']