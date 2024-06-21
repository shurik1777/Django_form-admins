from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'amount', 'photo']
        labels = {
            'title': 'Название продукта',
            'content': 'Описание',
            'price': 'Цена',
            'amount': 'Количество продукта',
            'photo': 'Фотография продукта'
        }
        help_texts = {
            'title': 'Укажите название продукта',
            'content': 'Укажите описание продукта',
            'price': 'Укажите цену продукта',
            'amount': 'Укажите количество продукта',
            'photo': 'Загрузите фотографию продукта (необязательно)'
        }
