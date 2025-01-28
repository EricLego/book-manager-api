class Book:
    def __init__(self, title, author, year):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
