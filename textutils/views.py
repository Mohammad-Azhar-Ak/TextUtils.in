# I have created this file- Azhar
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
     return render(request, 'about.html')
def contact(request):
     return render(request,'contact.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','off')
    capitalize= request.POST.get('capitalize','off')
    Newlineremover = request.POST.get('Newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = ''''/[-[\]{}()*+?.:;,'\\^$|#\]/g,"\\$&"'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        param = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if(capitalize=="on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
    if(Newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed + char
        param = {'purpose': 'NewLine Removed', 'analyzed_text': analyzed}
        djtext = analyzed
    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
           if not(djtext[index]==" " and djtext[index+1]==" "):
               analyzed = analyzed + char
        param = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        djtext = analyzed
    if(charcount=="on"):
        count=0
        spacecount=0
        for char in djtext:
            if(char==" "):
                spacecount=spacecount+1
            else:
                count=count+1
        param = {'purpose': 'Character Count', 'analyzed_text': djtext, 'counter':count, 'spaces':spacecount}
        return render(request,'analyze2.html',param)

    if(removepunc!="on"and extraspaceremover!="on"and Newlineremover!="on"and capitalize!="on"and charcount!="on"):
        return HttpResponse("Error! Please Select any operation")
    return render(request, 'analyze.html', param)


