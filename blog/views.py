from django.shortcuts import render

# Create your views here.
def bindex(request):
    # return HttpResponse("Index Shop")
    # params = {'purpose':'Remove Punctuations','analyzed_text':analyze}
    # return render(request,'analyse.html',params)
    return render(request,'bindex.html')