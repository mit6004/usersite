# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Quiz'
        db.create_table('tutorials_quiz', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('quiz_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('semester', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('tutorials', ['Quiz'])

        # Adding unique constraint on 'Quiz', fields ['semester', 'num']
        db.create_unique('tutorials_quiz', ['semester', 'num'])

        # Adding model 'Lab'
        db.create_table('tutorials_lab', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('submit_due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('checkoff_due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('semester', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('max_score', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('tutorials', ['Lab'])

        # Adding unique constraint on 'Lab', fields ['num', 'semester']
        db.create_unique('tutorials_lab', ['num', 'semester'])

        # Adding model 'PublicVideo'
        db.create_table('tutorials_publicvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('semester', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('tutorials', ['PublicVideo'])

        # Adding model 'TopicAssignment'
        db.create_table('tutorials_topicassignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutorials.PublicVideo'])),
            ('start_time', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('stop_time', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('num_staff_favorites', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('tutorials', ['TopicAssignment'])

        # Adding model 'Comment'
        db.create_table('tutorials_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clip', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['tutorials.TopicAssignment'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('permissions', self.gf('django.db.models.fields.CharField')(default='students', max_length=64)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('tutorials', ['Comment'])

        # Adding model 'LinkedWebPage'
        db.create_table('tutorials_linkedwebpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(default='http://6004.csail.mit.edu/currentsemester/', max_length=200)),
            ('topic_assignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutorials.TopicAssignment'])),
            ('pointer_on_page', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
        ))
        db.send_create_signal('tutorials', ['LinkedWebPage'])

        # Adding model 'UserProfile'
        db.create_table('tutorials_userprofile', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('athena_id', self.gf('django.db.models.fields.CharField')(max_length=8, primary_key=True)),
            ('student_id', self.gf('django.db.models.fields.IntegerField')(max_length=9, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('tutorials', ['UserProfile'])

        # Adding M2M table for field favorites on 'UserProfile'
        db.create_table('tutorials_userprofile_favorites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['tutorials.userprofile'], null=False)),
            ('topicassignment', models.ForeignKey(orm['tutorials.topicassignment'], null=False))
        ))
        db.create_unique('tutorials_userprofile_favorites', ['userprofile_id', 'topicassignment_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Lab', fields ['num', 'semester']
        db.delete_unique('tutorials_lab', ['num', 'semester'])

        # Removing unique constraint on 'Quiz', fields ['semester', 'num']
        db.delete_unique('tutorials_quiz', ['semester', 'num'])

        # Deleting model 'Quiz'
        db.delete_table('tutorials_quiz')

        # Deleting model 'Lab'
        db.delete_table('tutorials_lab')

        # Deleting model 'PublicVideo'
        db.delete_table('tutorials_publicvideo')

        # Deleting model 'TopicAssignment'
        db.delete_table('tutorials_topicassignment')

        # Deleting model 'Comment'
        db.delete_table('tutorials_comment')

        # Deleting model 'LinkedWebPage'
        db.delete_table('tutorials_linkedwebpage')

        # Deleting model 'UserProfile'
        db.delete_table('tutorials_userprofile')

        # Removing M2M table for field favorites on 'UserProfile'
        db.delete_table('tutorials_userprofile_favorites')


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
        'tutorials.comment': {
            'Meta': {'ordering': "['time']", 'object_name': 'Comment'},
            'clip': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['tutorials.TopicAssignment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permissions': ('django.db.models.fields.CharField', [], {'default': "'students'", 'max_length': '64'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'pointer_on_page': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'topic_assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tutorials.TopicAssignment']"}),
            'url': ('django.db.models.fields.URLField', [], {'default': "'http://6004.csail.mit.edu/currentsemester/'", 'max_length': '200'})
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
            'Meta': {'object_name': 'TopicAssignment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_staff_favorites': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_time': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'stop_time': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tutorials.PublicVideo']"})
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
