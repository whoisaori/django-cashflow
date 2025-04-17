from django import forms
from .models import Transaction, Category, SubCategory, Status, Type


class BaseSimpleForm(forms.ModelForm):
    class Meta:
        fields = '__all__'


class TransactionForm(forms.ModelForm):
    class Meta(BaseSimpleForm.Meta):
        model = Transaction
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')

        if subcategory.category != category:
            raise forms.ValidationError('Выбранная подкатегория не принадлежит выбранной категории.')

        if category.type != cleaned_data.get('type'):
            raise forms.ValidationError("Выбранная категория не принадлежит выбранному типу.")

        return cleaned_data


class StatusForm(forms.ModelForm):
    class Meta(BaseSimpleForm.Meta):
        model = Status


class TypeForm(forms.ModelForm):
    class Meta(BaseSimpleForm.Meta):
        model = Type


class CategoryForm(forms.ModelForm):
    class Meta(BaseSimpleForm.Meta):
        model = Category


class SubCategoryForm(forms.ModelForm):
    class Meta(BaseSimpleForm.Meta):
        model = SubCategory
