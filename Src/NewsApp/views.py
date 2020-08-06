from django.shortcuts import render
from newsapi import NewsApiClient
from pygooglenews import GoogleNews
from .models import NewsApp
# Create your views here.


def Home(request,*args,**kwargs):
    return render(request,"index.html",{})

def Index(request):
    article= NewsApp()
    newsapi=NewsApiClient(api_key="1b65d1e946504034a6bf74c18d1fde1f")
    headLines=newsapi.get_top_headlines(country="gb",category="technology")
    articles=headLines["articles"]



    news=[]
    description = []
    url=[]
    image=[]
    author=[]
    published=[]

    for i in range(len(articles)):
        newArtical=articles[i]
        news.append(newArtical["title"])
        description.append(newArtical["description"])
        url.append(newArtical["url"])
        image.append(newArtical["urlToImage"])
        author.append(newArtical["author"])
        published.append(newArtical["publishedAt"])
    article.title= newArtical["title"]
    article.description = description
    article.author = author
    article.publishedAt = published
    article.save()

    myList=zip(news,description,url,image,author,published)

    #  print(myList)
    return render(request,"bbc.html",context={"myList":myList})

def AlNews(request):
    newsapi=NewsApiClient(api_key="1b65d1e946504034a6bf74c18d1fde1f")
    headLines=newsapi.get_top_headlines(country="us",category="business")
    articles=headLines["articles"]


    news=[]
    description = []
    url=[]
    image=[]
    author=[]
    published=[]


    for i in range(len(articles)):
        newArtical=articles[i]
        news.append(newArtical["title"])
        description.append(newArtical["description"])
        url.append(newArtical["url"])
        image.append(newArtical["urlToImage"])
        author.append(newArtical["author"])
        published.append(newArtical["publishedAt"])

    mynews= zip(news,description,url,image,author,published)


    return render(request,"alJasira.html",context={"mynews":mynews})

def Gnew(request):
    gn=GoogleNews()
    topNews=gn.top_news()




