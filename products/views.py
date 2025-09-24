from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from . import models, forms
from categories.models import Category
from brands.models import Brand


class ProductListView(ListView):
    model = models.Product
    template_name = "product_list.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        category = self.request.GET.get("category")
        brand = self.request.GET.get("brand")

        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(serie_number__icontains=q))

        if category:
            queryset = queryset.filter(category__id=category)

        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["brands"] = Brand.objects.all()
        return context


class ProductCreateView(CreateView):
    model = models.Product
    template_name = "product_create.html"
    form_class = forms.ProductForm
    success_url = reverse_lazy("product_list")


class ProductDetailView(DetailView):
    model = models.Product
    template_name = "product_detail.html"


class ProductUpdateView(UpdateView):
    model = models.Product
    template_name = "product_update.html"
    form_class = forms.ProductForm
    success_url = reverse_lazy("product_list")


class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("product_list")
