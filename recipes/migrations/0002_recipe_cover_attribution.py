from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="cover_credit",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="recipe",
            name="cover_credit_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="cover_license_url",
            field=models.URLField(blank=True),
        ),
    ]
