# donations/migrations/0004_alter_donor_referral_code_alter_donor_referred_by.py
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_campaign_created_at_donor_referral_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='referral_code',
            field=models.CharField(max_length=20, unique=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='referred_by',
            field=models.ForeignKey(
                'self', related_name='referred_donors', on_delete=models.SET_NULL, null=True, blank=True
            ),
        ),
    ]
