from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def Home(request,*args,**kwargs):
    return render(request,"index.html",{})

def Index(request):
    newsapi=NewsApiClient(api_key="1b65d1e946504034a6bf74c18d1fde1f")
    headLines=newsapi.get_top_headlines(sources="bbc-news")
    articles=headLines["articles"]


    news=[]
    description = []
    image=[]
    author=[]
    published=[]

    for i in range(len(articles)):
        newArtical=articles[i]
        news.append(newArtical["title"])
        description.append(newArtical["description"])
        image.append(newArtical["urlToImage"])
        author.append(newArtical["author"])
        published.append(newArtical["publishedAt"])

    myList=zip(news,description,image,author,published)
    #  print(myList)
    return render(request,"bbc.html",context={"myList":myList})

def AlNews(request):
    newsapi=NewsApiClient(api_key="1b65d1e946504034a6bf74c18d1fde1f")
    headLines=newsapi.get_top_headlines(sources="al-jazeera-english")
    articles=headLines["articles"]


    news=[]
    description = []
    image=[]
    author=[]
    published=[]

    for i in range(len(articles)):
        newArtical=articles[i]
        news.append(newArtical["title"])
        description.append(newArtical["description"])
        image.append(newArtical["urlToImage"])
        author.append(newArtical["author"])
        published.append(newArtical["publishedAt"])

    mynews= zip(news,description,image,author,published)

    return render(request,"alJasira.html",context={"mynews":mynews})


