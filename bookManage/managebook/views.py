from django.shortcuts import render_to_response
from . models import Author,Book
# Create your views here.

def Manage(request):
    return render_to_response('Manage.html')
    
def SearchBook(request):
    return render_to_response('SearchBook.html')
    
def AddBook(request):
    return render_to_response('AddBook.html')

def AddAuthor(request):
    return render_to_response('AddAuthor.html')
    
def AddAuthorResult(request):
    if request.POST:
        author = Author()
        aID = request.POST["AuthorID"]
        allauthors = Author.objects.all()
        team = 0
        for authors in allauthors:
            if(aID == authors.AuthorID):
                 team = team + 1
        if(team):
            tag = 1
        else:
            author.AuthorID = request.POST["AuthorID"]
            author.Name = request.POST["Name"]
            author.Age = request.POST["Age"]
            author.Country = request.POST["Country"]
            author.save()
            tag = 0
        return render_to_response('AddAuthorResult.html',
                                  {'Name':author.Name ,'IsAuthor':tag})
    else:
        return render_to_response('AddAuthor.html')
        
def AddBookResult(request):
    book = Book()
    if request.POST:
        aID = request.POST["AuthorID"]
        allauthors = Author.objects.all()
        team = 0
        for authors in allauthors:
            if(aID == authors.AuthorID):
                 team = team + 1
        if(team):
            tag = 1
            book.ISBN = request.POST["ISBN"]
            book.Title = request.POST['Title']
            book.AuthorID = request.POST['AuthorID']
            book.Publisher = request.POST['Publisher']
            book.PublishDate = request.POST['Publishdate']
            book.Price = request.POST['Price']
            book.save()
        else:
            tag = 0;
        return render_to_response('AddBookResult.html',
                                  {'Book':book.Title,'IsBook':tag})
    else:
        return render_to_response('AddBook.html')

def SearchResult(request):
    if 'AuthorName' in request.GET:
        person = request.GET['AuthorName']
        books = []
        allauthors = Author.objects.all()
        team = 0
        for authors in allauthors:
            if(person == authors.Name):
                 team = team + 1
                 books = Book.objects.filter(AuthorID__icontains = authors.AuthorID)
        return render_to_response('SearchResult.html',{'bookname':books,'person':person,'tag':team})
    else:
        return render_to_response('SearchResult.html',  {'bookname':books})

def ShowBook(request):
    books = Book.objects.all()
    return render_to_response('ShowBook.html',{'allbooks':books })

def InformationBook(request,bookISBN):
    books = Book.objects.filter(ISBN__icontains = bookISBN)
    authors = Author.objects.filter(AuthorID__icontains = books[0].AuthorID)
    return render_to_response('InformationBook.html',
                              {'book':books[0],'author':authors[0]})
def DeleteBook(request,bookISBN):
    books = Book.objects.filter(ISBN__icontains = bookISBN)
    temp = books[0]
    books[0].delete()
    return render_to_response('DeleteBook.html',{'book':temp})
    
def UpdataBook(request,bookISBN):
    books = Book.objects.filter(ISBN__icontains = bookISBN)
    authors = Author.objects.filter(AuthorID__icontains = books[0].AuthorID)
    book = books[0]
    author = authors[0]
    books[0].delete()
    return render_to_response('UpdataBook.html',{'book':book,'author':author})




