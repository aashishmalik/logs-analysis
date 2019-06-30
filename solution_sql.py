#!/usr/bin/env python3

import psycopg2

if __name__=="__main__"
    try:
        db=psycopg2.connect(database="news")
        query=db.cursor()
        print("The list of most famous articles are as follows : \n")
        popularArticles(query)
        print("The most Popular Authors are: \n")
        popularAuthors(query)
        print("Days in which more than 1% of requests lead to errors: \n")
        errorDays(query)
        db.close()
    except psycopg2.DatabaseError, e:
        print(e)