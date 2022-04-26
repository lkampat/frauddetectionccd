from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import pickle
import os
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, "index.html")


def upload(request):
    return render(request, "upload.php")


def model_data(request):
    path='/CCDFD/newyoga/yoga/'
    file='test_preprocessed.csv'
    if os.path.exists(path+file):
        os.remove(path+file)

    '''os.remove('/CCDFD/newyoga/yoga/test_preprocessed.csv')'''

    if request.method == 'POST' and request.FILES['test_preprocessed']:
        test_preprocessed = request.FILES['test_preprocessed']
        fs = FileSystemStorage()
        filename = fs.save(test_preprocessed.name, test_preprocessed)
        newname = 'test_preprocessed.csv'
        os.rename(path+filename,path+newname)

        '''uploaded_file_url = fs.url(filename)'''
    return render(request, 'index.html')


'''return render(request,'index.html')'''

'''test_data_preprocessed = pd.read_csv('filename')'''
def Data_set(request):
    Sample_data = pd.read_csv('/CCDFD/newyoga/yoga/Sample_data.csv')
    filename = 'Sample_data.csv'
    response = HttpResponse(open(filename, 'rb').read(), content_type='text/csv')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename=%s' % 'Sample_data.csv'
    return response


def models(request):
    test_data_preprocessed = pd.read_csv('/CCDFD/newyoga/yoga/test_preprocessed.csv')
    if 'gNB' in request.POST:
        gaussian = pickle.load(open('gNB.sav', 'rb'))
        y_pred = gaussian.predict(test_data_preprocessed)
        output = pd.DataFrame(y_pred)
        output.to_csv('gaussianNB.csv')

        filename = 'gaussianNB.csv'
        response = HttpResponse(open(filename, 'rb').read(), content_type='text/csv')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'gaussianNB.csv'
        return response

    if 'lg' in request.POST:
        multi = pickle.load(open('lg.sav', 'rb'))
        y_pred = multi.predict(test_data_preprocessed)
        output = pd.DataFrame(y_pred)
        output.to_csv('lg.csv')

        filename = 'lg.csv'
        response = HttpResponse(open(filename, 'rb').read(), content_type='text/csv')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'lg.csv'
        return response

    if 'rfc' in request.POST:
        rf = pickle.load(open('rfc.sav', 'rb'))
        y_pred = rf.predict(test_data_preprocessed)
        output = pd.DataFrame(y_pred)
        output.to_csv('rfc.csv')

        filename = 'rfc.csv'
        response = HttpResponse(open(filename, 'rb').read(), content_type='text/csv')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'rfc.csv'
        return response
