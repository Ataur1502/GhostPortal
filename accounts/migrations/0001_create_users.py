from django.db import migrations
import secrets

def create_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    # Create guest user
    if not User.objects.filter(username='guest').exists():
        User.objects.create_user(
            username='guest',
            password='guest123',
            email='guest@ghostportal.local'
        )
    # Create admin user
    if not User.objects.filter(username='admin').exists():
        # Generate a highly secure random password not discoverable via brute force
        secure_password = secrets.token_urlsafe(32)
        User.objects.create_superuser(
            username='admin',
            password=secure_password,
            email='admin@ghostportal.local'
        )

def remove_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username__in=['guest', 'admin']).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__first__'),
    ]

    operations = [
        migrations.RunPython(create_users, reverse_code=remove_users),
    ]
