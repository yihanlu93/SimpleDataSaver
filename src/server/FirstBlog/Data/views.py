from django.shortcuts import render

# Create your views here.
from Data.models import data
from Data.models import tag
from Data.forms import BlogForm 
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from sys import getsizeof

def home(request):
	datas = data.objects.all()
	return render_to_response('index.html', {'datas' : datas, 'num' : len(datas)})

def post_form_upload(request):
    if request.POST:
        form = BlogForm(request.POST)
        if form.is_valid():
            d = form.save();

            if d.age < 18:
                t = tag(person=d, age_group='K')
                t.save()
            elif d.age >=18 & d.age <60:
                t = tag(person=d, age_group='A')
                t.save()
            else:
                t = tag(person=d, age_group='S')
                t.save()


            return HttpResponseRedirect('home')
    else:
        form = BlogForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('post_form_upload.html', args)

def about(request):
    return render_to_response('about.html',request)

def clear(request):
    data.objects.all().delete()
    datas = data.objects.all()
    return render_to_response('index.html', {'datas' : datas, 'num' : len(datas)})
