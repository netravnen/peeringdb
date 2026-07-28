import django.db.models.deletion
import django_handleref.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "peeringdb_server",
            "0153_alter_ixfmemberdata_speed_alter_networkixlan_speed_and_more",
        ),
        ("reversion", "0002_add_index_on_version_for_content_type_and_db"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FacilityOwnershipTransferRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_handleref.models.CreatedDateTimeField(
                        auto_now_add=True, verbose_name="Created"
                    ),
                ),
                (
                    "reason",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Why this transfer was initiated, in the initiating admin's own words",
                        max_length=255,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="pending",
                        help_text="Status of this request",
                        max_length=32,
                    ),
                ),
                (
                    "fac",
                    models.ForeignKey(
                        help_text="The facility to be transferred",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transfer_requests",
                        to="peeringdb_server.facility",
                    ),
                ),
                (
                    "requested_by",
                    models.ForeignKey(
                        help_text="The user that initiated the transfer",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "source_org",
                    models.ForeignKey(
                        help_text="The organization the facility is transferred from. Recorded explicitly rather than read from fac.org, which changes when the transfer is approved.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="peeringdb_server.organization",
                    ),
                ),
                (
                    "target_org",
                    models.ForeignKey(
                        help_text="The organization the facility is to be transferred to",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="peeringdb_server.organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Facility Ownership Transfer Request",
                "verbose_name_plural": "Facility Ownership Transfer Requests",
                "db_table": "peeringdb_facility_ownership_transfer_request",
            },
        ),
        migrations.CreateModel(
            name="FacilityOwnershipTransferRequestHistory",
            fields=[],
            options={
                "verbose_name": "Facility Ownership Transfer Request History",
                "verbose_name_plural": "Facility Ownership Transfer Request History",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("reversion.version", models.Model),
        ),
    ]
