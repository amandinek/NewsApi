from django.shortcuts import render
from newsapi import NewsApiClient
# from pygooglenews import GoogleNews
from .models import NewsApp
# Create your views here.


def Home(request,*args,**kwargs):
    return render(request,"index.html",{})

def Index(request):
    # article= NewsApp()
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


    myList=zip(news,description,url,image,author,published)
    article = NewsApp(title=news, description=description,author=author, publishedAt=published)
    article.save()
    print("article saved")
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








