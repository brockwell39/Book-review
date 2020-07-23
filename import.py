import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    count = 0
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn,author,title,year) VALUES (:isbn,:author,:title,:year)",
        {"isbn": isbn,"author": author, "title": title,"year": year})
        count += 1
    db.commit()
    print("Records added ",count)

if __name__ == '__main__':
    main()
