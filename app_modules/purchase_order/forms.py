from django import forms
from app_modules.purchase_order.models import PurchaseOrder,PurchaseOrderProducts
from app_modules.company.models import Company, Warehouse
from app_modules.users.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError

# from django.urls import reverse


class PurchaseOrderFrom(forms.ModelForm):
    warehouse_id = forms.ChoiceField(required=False, label="warehouse", choices=[])

    class Meta:
        model = PurchaseOrder
        fields = ("company","vendor","bill_number","bill_date","remarks","total_price","invoice",'status', 'warehouse_id')
        widgets={
                'remarks' : forms.Textarea(attrs={'rows':4 ,'class':'form-control'}),
                'bill_date' :forms.DateInput(format = '%-d %B, %Y'),
                
        }

    def __init__(self,user,*args,**kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = self.fields['company'].queryset.exclude(status=Company.IS_INACTIVE)
        self.fields['warehouse_id'].queryset = Warehouse.objects.all()

        if self.user.role == User.COMPANY_ADMIN or self.user.role == User.SALES_REPRESENTATIVE:
            self.fields.pop('company')


        if kwargs["instance"]:
            self.fields['status'].required = True
            # self.fields["company"].widget.attrs.update({"disabled": "disabled"})
            # self.fields["vendor"].widget.attrs.update({"disabled": "disabled"})
            pass
        else:
            self.fields['status'].required = False

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs["placeholder"] = visible.field.label

        if self.instance and self.instance.pk and self.instance.status == PurchaseOrder.COMPLETED:
            self.fields['status'].choices = ((PurchaseOrder.COMPLETED, "Completed"), (PurchaseOrder.REVERTED, "Reverted"))
            # self.fields['company'].widget.value_from_datadict = lambda *args: self.instance.company
            self.fields['vendor'].widget.value_from_datadict = lambda *args: self.instance.vendor
            self.fields['bill_number'].widget.value_from_datadict = lambda *args: self.instance.bill_number
            self.fields['bill_date'].widget.value_from_datadict = lambda *args: self.instance.bill_date
            self.fields['remarks'].widget.value_from_datadict = lambda *args: self.instance.remarks
            self.fields['total_price'].widget.value_from_datadict = lambda *args: self.instance.total_price
            self.fields['invoice'].widget.value_from_datadict = lambda *args: self.instance.invoice
            for visible in self.visible_fields():
                if visible.field.label.lower() != "status":
                    visible.field.widget.attrs['disabled'] = 'disabled'

        self.fields["vendor"].widget.attrs.update({"class": "form-control select2"})
        
        self.fields["vendor"].required = True
        self.fields["bill_date"].widget.attrs.update({"class": "form-control pickadate-selectors picker__input"})
        self.fields["invoice"].widget.attrs.update({"class": "custom-file-input"})
        self.fields["total_price"].widget.attrs.update({"class": "form-control text-center"})
        self.fields["total_price"].widget.attrs.update({"readonly": "readonly"})

        
        if self.user.role == User.SUPER_ADMIN:
            self.fields["company"].widget.attrs["class"] = "select2-data-array form-control category-list"
            self.fields["company"].required = True
            # self.fields["company"].widget.attrs.update({"data-url": reverse('purchase_order:ajax_get_vendors_by_company')})

    # def clean_warehouse_id(self):
    #     status = self.cleaned_data.get("status")
    #     warehouse = self.cleaned_data.get("warehouse_id")
    #     if not warehouse and status == PurchaseOrder.COMPLETED:
    #         raise ValidationError("This field is required.")
    #     return warehouse

class PurchaseOrderProductsForm(forms.ModelForm):
    SELECT = ""

    CHOICES = (
        (SELECT, "---------"),
    )
    unit_type = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = PurchaseOrderProducts
        fields = ("product","unit_type","quantity","total_pieces","cost_price")

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        # widgets = {
        #     'unit_type':forms.Cho(choices=self.choices)
        # }

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs["placeholder"] = visible.field.label
        self.fields["product"].widget.attrs.update({"class": "form-control select2"})
        self.fields["product"].widget.attrs.update({"data-url": reverse('purchase_order:ajax_get_product_details')})

        # self.fields[''] = forms.ChoiceField(choices=self.choices)
        self.fields["unit_type"].widget.attrs.update({"class": "form-control select2"})
        self.fields["quantity"].widget.attrs.update({"min": "1","step": "1"})
        self.fields["cost_price"].widget.attrs.update({"min": "0.00"})
        self.fields["cost_price"].widget.attrs.update({"step": "0.01"})
        self.fields['total_pieces'].widget.attrs['readonly'] = True
