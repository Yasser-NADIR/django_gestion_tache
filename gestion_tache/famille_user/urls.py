from django.urls import path
from .views import index, add_f_user, edit_f_user, delete_f_user, download_f_users_html, download_f_users_csv, download_f_user_pdf, download_f_users_list_pdf

urlpatterns = [
    path('', index, name='f_users'),
    path('add/', add_f_user, name='add_f_user'),
    path('edit/<int:id>', edit_f_user, name='edit_f_user'),
    path('delete/<int:id>', delete_f_user, name='delete_f_user'),
    path('download_html', download_f_users_html, name='download_f_users_html'),
    path('download_csv', download_f_users_csv, name='download_f_users_csv'),
    path('downlaod_pdf/<int:id>', download_f_user_pdf, name='download_f_user_pdf'),
    path('download_pdf_list', download_f_users_list_pdf, name='download_f_users_list_pdf'),
]