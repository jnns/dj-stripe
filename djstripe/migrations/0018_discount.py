# Generated by Django 3.2.16 on 2023-01-28 06:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import djstripe.fields


class Migration(migrations.Migration):
    dependencies = [
        ("djstripe", "0017_invoiceorlineitem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                ("created", djstripe.fields.StripeDateTimeField(blank=True, null=True)),
                ("metadata", djstripe.fields.JSONField(blank=True, null=True)),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A description of this object.", null=True
                    ),
                ),
                ("coupon", djstripe.fields.JSONField(blank=True, null=True)),
                ("end", djstripe.fields.StripeDateTimeField(blank=True, null=True)),
                (
                    "promotion_code",
                    models.CharField(
                        blank=True,
                        help_text="The promotion code applied to create this discount.",
                        max_length=255,
                    ),
                ),
                ("start", djstripe.fields.StripeDateTimeField(blank=True, null=True)),
                (
                    "checkout_session",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.session",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "customer",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The ID of the customer associated with this discount.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer_discounts",
                        to="djstripe.customer",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The Stripe Account this object belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "invoice",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoice_discounts",
                        to="djstripe.invoice",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "invoice_item",
                    djstripe.fields.InvoiceOrLineItemForeignKey(
                        blank=True,
                        help_text="The invoice item id (or invoice line item id for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.invoiceorlineitem",
                    ),
                ),
                (
                    "subscription",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The subscription that this coupon is applied to, if it is applied to a particular subscription.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscription_discounts",
                        to="djstripe.subscription",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
    ]