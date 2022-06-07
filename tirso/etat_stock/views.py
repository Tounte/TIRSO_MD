import json
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from etat_stock.models import Excel,Clients,Destination,Origine,Transporteur
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from etat_stock.forms import ExcelForm
from django.core.files.storage import FileSystemStorage
import pandas as pd
import matplotlib as plt
import numpy as np


@login_required(login_url='login')
def stock(request):
    files_list=Excel.objects.all()
    return render(request,"files-index.html",{"files_list":files_list})

@login_required(login_url='login')
def master_data(request):
    if request.method == 'POST':
        upload_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(upload_file.name, upload_file)
        url=fs.url(name)
        print(url)
        url = url[1:]
        data=pd.read_excel(url)
        dfc=data['Client']
        print(dfc)





    return render(request, 'master-data.html')


@login_required(login_url='login')
def upload_file(request):
    if request.method == 'POST':
        form= ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('files_index')
    else:
        form= ExcelForm()
    return render(request,'upload-file.html',{'form':form,})

@login_required(login_url='login')
def check_file(request, id):
    file= Excel.objects.get(id=id)
    data_file=pd.read_excel(file.file)
    c=list(data_file.columns)
    df=data_file
    new_df=df.assign(Statut1=0,Statut2=0,Statut3=0,Statut4=0)
    clients_list=Clients.objects.all()
    transporteur_list=Transporteur.objects.all()
    origine_list=Origine.objects.all()
    destination_list=Destination.objects.all()

    for i in new_df.index:
        for j in clients_list:
            a = j.clients
            b = new_df['Client'][i]
            if a == b:
                new_df['Statut1'][i]=1
                break

        for j in transporteur_list:
            a = j.transporter
            b = new_df['Transporteur'][i]
            if a == b:
                new_df['Statut2'][i]=1
                break
        
        for j in origine_list :
            a = j.origin
            b = new_df['Origine'][i]
            if a == b:
                new_df['Statut3'][i]=1
                break

        for j in destination_list:
            a = j.destination
            b = new_df['Destination'][i]
            if a == b:
                new_df['Statut4'][i]=1
                break
    
    json_records = new_df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    print(new_df)
    return render(request,"check-file.html",context)

@login_required(login_url='login')
def delete_file(request, id):
    file= Excel.objects.get(id=id)
    file.delete()
    return redirect("/")


