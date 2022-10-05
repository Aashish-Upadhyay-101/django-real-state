# Generated by Django 4.1 on 2022-10-05 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="propertyviews",
            options={
                "verbose_name": "Total Views on Property",
                "verbose_name_plural": "Total Property Views",
            },
        ),
        migrations.AddField(
            model_name="propertyviews",
            name="property",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="property_views",
                to="properties.property",
            ),
        ),
    ]
