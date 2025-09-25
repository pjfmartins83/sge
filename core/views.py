from django.shortcuts import render
from . import metrics


def home(request):
    product_metrics = metrics.get_metric_products()
    sales_metrics = metrics.get_sales_metrics()

    context = {
        "product_metrics": product_metrics,
        "sales_metrics": sales_metrics,
    }
    return render(request, "home.html", context)
