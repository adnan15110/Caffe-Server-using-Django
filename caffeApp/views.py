# from django.http import HttpResponse
# from django.template import RequestContext, loader
# from django.template import loader
from django.shortcuts import render
from .caffe_models.test_class import test_class
# Create your views here.


def index(request):
    instance = test_class()
    data = instance.functionOne()
    # emplate = loader.get_template('caffeApp/index.html')
    # context = RequestContext(request, {
    #     'classication_data': data,
    # })
    # return HttpResponse(template.render(context))
    context = {'classication_data': data}
    return render(request, 'caffeApp/index.html', context)


def image_app(request):
    instance = test_class()
    data = instance.functionOne()
    # emplate = loader.get_template('caffeApp/index.html')
    # context = RequestContext(request, {
    #     'classication_data': data,
    # })
    # return HttpResponse(template.render(context))
    if request.POST.get('choice', False):
        context = {'classication_data': data, 'post_data': request.POST.get('choice', False)}
    else:
        context = {'classication_data': data}
    return render(request, 'caffeApp/image_app.html', context)
