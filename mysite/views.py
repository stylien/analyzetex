import imp
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def analyzer(request):
    djtext = request.POST.get('text','default')
    removepun = request.POST.get('removepunc','off')
    capatalized = request.POST.get('capitalize','off')
    newlineremover = request.POST.get('newlineremove','off')
    charactercount = request.POST.get('charactercount','off')
    if removepun=="on":
        punctuation = '''!@#$%^&*()-;:'"/?.,<>'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        param = {'purpose':'Remove Punctuation','analyzed_text':analyzed}
        djtext=analyzed
    if capatalized=='on':
        analyzed = djtext.upper()
        param = {'purpose':'Upper Case','analyzed_text':analyzed}
        djtext=analyzed
    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            if (char !="\n" and char !="\r") :
                analyzed = analyzed + char
        param = {'purpose':'Remove New Line','analyzed_text':analyzed}
        djtext=analyzed
    if charactercount =='on':
        sum=0
        for char in djtext:
            if char != " ":
                sum = sum +1
        return HttpResponse(sum)
    if(charactercount !='on' and newlineremover != "on" and capatalized !='on' and removepun !="on"):
        return HttpResponse( "Error ")
    return render(request,'punc.html',param)
