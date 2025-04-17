from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),

     #  Transaction
     path('create/',
          views.transaction_create,
          name='transaction_create'),
     path('edit/<int:pk>/',
          views.transaction_edit,
          name='transaction_edit'),
     path('delete/<int:pk>/',
          views.transaction_delete,
          name='transaction_delete'),

     # пути для js
     path('load-categories/',
          views.load_categories,
          name='load_categories'),
     path('load-subcategories/',
          views.load_subcategories,
          name='load_subcategories'),
]


def generate_crud_patterns(entity_name, view_prefix):
    return [
          path(f'create/{entity_name}/',
               getattr(views, f'{view_prefix}_create'),
               name=f'{entity_name}_create'),

          path(f'edit/{entity_name}/<int:pk>/',
               getattr(views, f'{view_prefix}_edit'),
               name=f'{entity_name}_edit'),

          path(f'delete/{entity_name}/<int:pk>/',
               getattr(views, f'{view_prefix}_delete'),
               name=f'{entity_name}_delete'),
     ]


urlpatterns += (
     generate_crud_patterns('status', 'status') +
     generate_crud_patterns('type', 'type') +
     generate_crud_patterns('cats', 'cats') +
     generate_crud_patterns('subcats', 'subcats')
)
