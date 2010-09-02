# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LinkedWebPage'
        db.create_table('tutorials_linkedwebpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('topic_assignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutorials.TopicAssignment'])),
        ))
        db.send_create_signal('tutorials', ['LinkedWebPage'])


    def backwards(self, orm):
        
        # Deleting model 'LinkedWebPage'
        db.delete_table('tutorials_linkedwebpage')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tutorials.annotation': {
            'Meta': {'object_name': 'Annotation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'stop_time': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tutorials.PublicVideo']"})
        },
        'tutorials.comment': {
            'Meta': {'object_name': 'Comment', '_ormbases': ['tutorials.Annotation']},
            'annotation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['tutorials.Annotation']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'tutorials.lab': {
            'Meta': {'ordering': "['num']", 'unique_together': "(('num', 'semester'),)", 'object_name': 'Lab'},
            'checkoff_due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_score': ('django.db.models.fields.FloatField', [], {}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'submit_due_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'tutorials.linkedwebpage': {
            'Meta': {'object_name': 'LinkedWebPage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic_assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tutorials.TopicAssignment']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'tutorials.publicvideo': {
            'Meta': {'object_name': 'PublicVideo'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '7'})
        },
        'tutorials.quiz': {
            'Meta': {'ordering': "['num']", 'unique_together': "(('semester', 'num'),)", 'object_name': 'Quiz'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'quiz_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'tutorials.topicassignment': {
            'Meta': {'object_name': 'TopicAssignment', '_ormbases': ['tutorials.Annotation']},
            'annotation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['tutorials.Annotation']", 'unique': 'True', 'primary_key': 'True'}),
            'num_staff_favorites': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'tutorials.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'athena_id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'favorites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tutorials.TopicAssignment']", 'null': 'True', 'blank': 'True'}),
            'student_id': ('django.db.models.fields.IntegerField', [], {'max_length': '9', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['tutorials']
