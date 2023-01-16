from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    a = {'name': "yeeshu"}
    return render(request, 'index.html', a)


def about(request):
    return HttpResponse("About <a href='/'>back</a>")


f = open('yes.txt')
data = f.read()
print(data)


def about2(request):
    return HttpResponse(data)


def personalNavigator(request):
    return HttpResponse('''<h1><a href="https://www.youtube.com">Youtube</a></h1>
    <h1><a href="https://www.codewithharry.com">CodeWithHarry</a></h1>
    <h1><a href="https://www.facebook.com">Facebook</a></h1>
    <h1><a href="https://www.google.com">Google</a></h1>
    <h1><a href="https://www.yahoo.com">Yahoo</a></h1>
    <h1><a href="https://www.twitter.com">Twitter</a></h1>''')


def analyzeText(request):
    djText = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newline = request.GET.get('newline', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    params = {
            'analyzed_text': djText
        }
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djText = analyzed
        # return render(request, 'analyze.html', params)


    if fullcaps == 'on':
        analyzed = ""
        for char in djText:
            analyzed += char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        djText = analyzed
        # return render(request, 'analyze.html', params)


    if newline == 'on':
        analyzed = ""
        for char in djText:
            if char != "\n" and char != "\r":
                analyzed += char
            if char == "\n":
                analyzed += " "
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djText = analyzed
        # return render(request, 'analyze.html', params)


    if spaceremover == 'on':
        # analyzed = ""
        # for index, char in enumerate(djText):
        #     if not (djText[index] == " " and djText[index + 1] == " "):
        #         analyzed = analyzed + char
        # params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        # djText = analyzed
        analyzed = ""
        for index, char in enumerate(djText):
            if index < (len(djText) - 1):
                if not (djText[index] == " " and djText[index + 1] == " "):
                    analyzed += char

            elif djText[index] != " ":
                analyzed += char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        djText = analyzed
        # return render(request, 'analyze.html', params)


    if charcount == 'on':
        # count = 0
        # for i in djText:
        #     count += 1
        count = len(djText)
        params = {
            'purpose': 'Number of Characters',
            'analyzed_text': djText,
            'count_text': count
        }
        # return render(request, 'analyze.html', params)

    # if (removepunc != "on" and newline!="on" and spaceremover!="on" and fullcaps!="on" and charcount!="on"):
    #     return HttpResponse("please select any operation and try again")


    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")
