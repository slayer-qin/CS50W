Web Programming with Python and JavaScript


# Project 0

Project0 Finished


1. four html files, index.html, games.html, flowers.html and learn.html
2. there are a nav bar in the top of every page linking to each other.
3. use list(navbar) and table in index.html.
4. use img in flowers.html.
5. there are two css files. style.css is for index.html,games.html and flowers.html.
6. use Bootstrap 4 in learning.html, and use mycustom.css for self-customed styles. using two Bootstrap components, Nav and Card.
7. use scss to make mycustom.css

# Project 1
Project1 Finished

- use ==flask== and ==psql== create a web site about book.
- Registration: Users should be able to register for your website, providing (at minimum) a username and password.
- Login: Users, once registered, should be able to log in to your website with their username and password.
- Logout: Logged in users should be able to log out of the site.
- Import: Provided for you in this project is a file called books.csv, which is a spreadsheet in CSV format of 5000 different books. Each one has an ISBN nubmer, a title, an author, and a publication year. In a Python file called import.py separate from your web application, write a program that will take the books and import them into your PostgreSQL database. You will first need to decide what table(s) to create, what columns those tables should have, and how they should relate to one another. Run this program by running python3 import.py to import the books into your database, and submit this program with the rest of your project code.
- Search: Once a user has logged in, they should be taken to a page where they can search for a book. Users should be able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, your website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, your search page should find matches for those as well!
- Book Page: When users click on a book from the results of the search page, they should be taken to a book page, with details about the book: its title, author, publication year, ISBN number, and any reviews that users have left for the book on your website.
- Review Submission: On the book page, users should be able to submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. Users should not be able to submit multiple reviews for the same book.
