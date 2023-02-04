# Generated by Django 4.1.3 on 2023-01-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cjkcms", "0004_layoutsettings_articles_date_format_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="layoutsettings",
            name="custom_font",
            field=models.BooleanField(
                default=False,
                help_text="Custom body font e.g. from CDN & include css body override",
                verbose_name="Use custom font",
            ),
        ),
        migrations.AddField(
            model_name="layoutsettings",
            name="font_family",
            field=models.CharField(
                blank=True,
                default="Roboto, sans-serif",
                help_text="Font family name, e.g. 'Open Sans, sans-serif'",
                max_length=128,
                verbose_name="Font Family",
            ),
        ),
        migrations.AddField(
            model_name="layoutsettings",
            name="font_url",
            field=models.CharField(
                blank=True,
                default="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap",
                help_text="Full URL to font css file",
                max_length=250,
                verbose_name="Font URL",
            ),
        ),
        migrations.AlterField(
            model_name="layoutsettings",
            name="awesome_cdn",
            field=models.BooleanField(
                default=False,
                help_text="Load font awesome from CDN",
                verbose_name="Font Awesome",
            ),
        ),
    ]