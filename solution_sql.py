#!/usr/bin/env python3

import psycopg2


def popularArticles(query)
    article_query='''select title, rslt.count from (
        select path, count(path) from (
            select * from log where status = '200 OK' and path != '/'
            ) as tbl
            group by path order by count(path) desc limit 3
        ) as rslt
        join articles on rslt.path like '%' || slug || '%' order by
        rslt.count desc;'''
    query.execute(article_query)
    for (name,count) in query.fetchall():
        print("{} - {} views ".format(name,count))
    print("-" * 80)

 def popularAuthors(query)
    authors_query='''select name, sum(rslt_two.count) as num
        from (select author, rslt.count from (
        select path, count(path) from (
            select * from log where status = '200 OK' and path != '/'
            ) as tab
            group by path
        ) as rslt
        join articles on rslt.path like '%' || slug || '%') as rslt_two
        join authors on rslt_two.author = authors.id
        group by name order by num desc;'''
    query.execute(authors_query)
    for (name, count) in query.fetchall():
        print("    {} - {} views".format(name, count))
    print("-" * 80)




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