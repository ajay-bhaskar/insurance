from django.db import models
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

def validate_premium(value):
    if value > 1000000:
        raise ValidationError('%s should not be more than 1 Million' % value)

class insuranceData (models.Model):
    policy_id = models.IntegerField(_("Policy_id"))
    date_of_purchase = models.DateField(_("Date of Purchase"), auto_now=True)
    customer_id	 = models.IntegerField(_("Customer_id"))
    fuel = models.CharField(_("Fuel"), max_length=255)
    vehicle_segment  = models.CharField(_("VEHICLE_SEGMENT"), max_length=255)
    premium = models.IntegerField(_("Premium"),validators=[validate_premium])
    bodily_injury_liability = models.IntegerField(_("bodily injury liability"))
    personal_injury_protection = models.IntegerField(_("personal injury protection"))
    property_damage_liability = models.IntegerField(_("property damage liability"))
    collision = models.IntegerField(_("collision"))
    comprehensive = models.IntegerField(_("comprehensive"))
    customer_gender = models.CharField(_("Customer_Gender"), max_length=255)
    customer_income_group = models.CharField(_("Customer_Income group"), max_length=255)
    customer_region = models.CharField(_("Customer_Region"), max_length=255)
    customer_marital_status = models.IntegerField(_("Customer_Marital_status"))
    class Meta:
        db_table="policy_insurancedata"

 

