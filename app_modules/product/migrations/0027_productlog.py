# Generated by Django 4.1.7 on 2023-07-17 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("credit_memo", "0007_creditmemolog"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0026_remove_product_box_upc_remove_product_case_upc_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("remark", models.TextField(verbose_name="Remark")),
                (
                    "action_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Action By",
                    ),
                ),
                (
                    "credit_memo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="credit_memo.creditmemo",
                        verbose_name="Credit Memo",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
