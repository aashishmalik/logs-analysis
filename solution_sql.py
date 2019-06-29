#!/usr/bin/env 

import psycopg2

if __name__=="__main__"
    try:
        db=psycopg2.connect(database="news")
        