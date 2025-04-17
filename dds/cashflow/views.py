from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import JsonResponse
from .models import Transaction, Type, Status, Category, SubCategory
from .forms import (TransactionForm,
                    TypeForm,
                    StatusForm,
                    CategoryForm,
                    SubCategoryForm)


def index(request):
    transactions = Transaction.objects.all().order_by('-date_created')
    context = {
        'transactions': transactions,
    }
    return render(request, 'cashflow/index.html', context=context)


def transaction_create(request):
    form = TransactionForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid() and form.clean():
        form.save()
        return redirect('index')
    return render(request, 'cashflow/transaction_form.html', context=context)


def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction)
    context = {
        'form': form,
        'transaction': transaction,
    }
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'cashflow/transaction_form.html', context=context)


def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    context = {
        'transaction': transaction,
    }
    if request.method == 'POST':
        transaction.delete()
        return redirect('index')
    return render(request,
                  'cashflow/transaction_confirm_delete.html',
                  context=context)


# AJAX обработчики для js, чтобы выводить только связанные поля
def load_categories(request):
    type_id = request.GET.get('type')
    categories = Category.objects.filter(type_id=type_id).order_by('name')
    return JsonResponse(list(categories.values('id', 'name')), safe=False)


def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = SubCategory.objects.filter(
        category_id=category_id).order_by('name')
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)


# Универсальная функция для CRUD
def crud_create(request, form_class, template_name, success_url):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})


def crud_edit(request, instance, form_class, template_name, success_url):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    return render(request, template_name, {'form': form})


def crud_delete(request, instance, success_url, template_name='confirm_delete.html'):
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    return render(request, template_name, {'object': instance})


# Status
def status_create(request):
    return crud_create(request, StatusForm, 'form.html', '/')


def status_edit(request, pk):
    instance = get_object_or_404(Status, pk=pk)
    return crud_edit(request, instance, StatusForm, 'form.html', '/')


def status_delete(request, pk):
    instance = get_object_or_404(Status, pk=pk)
    return crud_delete(request, instance, '/')


# Type
def type_create(request):
    return crud_create(request, TypeForm, 'form.html', '/')


def type_edit(request, pk):
    instance = get_object_or_404(Type, pk=pk)
    return crud_edit(request, instance, TypeForm, 'form.html', '/')


def type_delete(request, pk):
    instance = get_object_or_404(Type, pk=pk)
    return crud_delete(request, instance, '/')


# Category
def cats_create(request):
    return crud_create(request, CategoryForm, 'form.html', '/')


def cats_edit(request, pk):
    instance = get_object_or_404(Category, pk=pk)
    return crud_edit(request, instance, CategoryForm, 'form.html', '/')


def cats_delete(request, pk):
    instance = get_object_or_404(Category, pk=pk)
    return crud_delete(request, instance, '/')


# Subcategory
def subcats_create(request):
    return crud_create(request, SubCategoryForm, 'form.html', '/')


def subcats_edit(request, pk):
    instance = get_object_or_404(SubCategory, pk=pk)
    return crud_edit(request, instance, SubCategoryForm, 'form.html', '/')


def subcats_delete(request, pk):
    instance = get_object_or_404(SubCategory, pk=pk)
    return crud_delete(request, instance, '/')
