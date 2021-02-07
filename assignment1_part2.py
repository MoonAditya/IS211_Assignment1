# Final version of Assignment 1, part 2
class Book:
    def __init(self, author, title):
      self.author = author
      self.title = title

    def display(self, title, author):  
      msg = "'{}', written by {}"
      print(msg.format(title, author))

        
if __name__ == "__main__":  
  title = ['Of Mice and Men', 'To Kill a Mockingbird']
  author = ['John Steinbeck', 'Harper Lee']
  test = Book()
  test.display(title[0], author[0])
  test.display(title[1], author[1])
