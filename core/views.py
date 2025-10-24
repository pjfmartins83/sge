import json
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import forms
from . import metrics


class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = forms.RegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # Salva o usuário:
        user = form.save()
        # Faz login automático:
        login(self.request, user)
        return super().form_valid(form)


@login_required(login_url="login")
def home(request):
    product_metrics = metrics.get_metric_products()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()

    context = {
        "product_metrics": product_metrics,
        "sales_metrics": sales_metrics,
        "daily_sales_data": json.dumps(daily_sales_data),
        "daily_sales_quantity_data": json.dumps(daily_sales_quantity_data),
        "product_count_by_category": json.dumps(graphic_product_category_metric),
        "product_count_by_brand": json.dumps(graphic_product_brand_metric),
    }
    return render(request, "home.html", context)
