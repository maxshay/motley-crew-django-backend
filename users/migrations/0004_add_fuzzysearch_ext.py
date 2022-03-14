from django.db import migrations, models
from django.contrib.postgres.operations import TrigramExtension

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_profile_image'),
    ]

    operations = [
        TrigramExtension()
    ]
