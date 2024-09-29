from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import FUser
from .forms import FUserForm
import csv
from xhtml2pdf import pisa
from io import BytesIO

def index(request):
    if request.method == 'POST':
        form = FUserForm(request.POST)
        if form.is_valid():
            f_users = FUser.objects\
                .filter(libelle_famille__icontains=form.cleaned_data['libelle_famille'])\
                .filter(coefficient__icontains=form.cleaned_data['coefficient'])\
                .filter(remarques__icontains=form.cleaned_data['remarques'])\
                .all
        else:
            print(form.errors)
            f_users = FUser.objects.all()
    else:
        form = FUserForm()
        f_users = FUser.objects.all()
    return render(request, 'f_user/index.html', {'f_users': f_users, 'form': form})

def add_f_user(request):
    if request.method == 'POST':
        form = FUserForm(request.POST)
        if form.is_valid():
            FUser.objects.create(
                libelle_famille = form.cleaned_data['libelle_famille'],
                coefficient = form.cleaned_data['coefficient'],
                remarques = form.cleaned_data['remarques']
            )
            return redirect('f_users')
    form = FUserForm()
    return render(request, 'f_user/add_f_user.html', {'form': form})

def edit_f_user(request, id):
    f_user = FUser.objects.get(id_f_user=id)
    if request.method == 'POST':
        form = FUserForm(request.POST)
        if form.is_valid():
            update_f_user = form.save(commit=False)
            update_f_user.id_f_user = id
            update_f_user.save()
            return redirect('f_users')
    form = FUserForm(instance=f_user)
    return render(request, 'f_user/edit_f_user.html', {'form': form})

def delete_f_user(request, id):
    FUser.objects.get(id_f_user=id).delete()
    return redirect('f_users')

def download_f_users_html(request):
    f_users = FUser.objects.all()
    html_content = render_to_string('f_user/f_user_list.html', {'users': f_users})
    responce = HttpResponse(html_content, content_type='text/html')
    responce['Content-Disposition'] = 'attachement; filename="f_users.html"'
    return responce

def download_f_users_csv(request):
    f_users = FUser.objects.all()

    responce = HttpResponse(content_type='text/csv')
    responce['Content-Disposition'] = 'attachement; filename="f_users.csv"'

    writer = csv.writer(responce)
    writer.writerow(['code famille', 'libelle_famille','coefficient','remarques'])
    for user in f_users:
        writer.writerow([user.id_f_user, user.libelle_famille, user.coefficient, user.remarques])
    return responce

def download_f_user_pdf(request, id):
    f_user = FUser.objects.get(id_f_user=id)
    html_content = render_to_string('f_user/f_user_pdf.html', {'user': f_user})
    pdf = BytesIO()
    pisa.CreatePDF(html_content, pdf)
    responce = HttpResponse(pdf.getvalue(), content_type='application/pdf')
    responce['Content-Disposition'] = 'attachement; filename=f_users.pdf'
    return responce

def download_f_users_list_pdf(request):
    f_users = FUser.objects.all()
    html_content = render_to_string('f_user/f_user_list_pdf.html', {'users': f_users})
    pdf = BytesIO()
    pisa.CreatePDF(html_content, pdf)
    responce = HttpResponse(pdf.getvalue(), content_type='application/pdf')
    responce['Content-Disposition'] = 'attachement; filename=f_users.pdf'
    return responce