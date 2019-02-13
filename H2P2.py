title = input ("Please enter the book title:   ")
author = input ("Please enter the author's name:   ")
bookYear = int (input ("Please enter the year the book was published:   "))
pages = int (input ("Please enter the number of pages in the book:   "))
currentYear = 2019
bookAge = currentYear - bookYear
if(bookAge < 10):
    print ("This book is younger than 10 years old")
else:
    print ("This book is at least 10 years old")

if(pages < 100):
    print ("This book is a short book")
elif(pages < 300):
    print ("This book is an average book")
else:
    print ("This book is a long book")
