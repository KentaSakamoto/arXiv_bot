#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests
import pickle
import os

def parse(data, tag):
    pattern = "<" + tag + ">([\s\S]*?)<\/" + tag + ">"
    if all:
        obj = re.findall(pattern, data)
    return obj

def serch_and_send(query, start, ids, api_url):
    while True:
        counter = 0
        url = 'http://export.arxiv.org/api/query?search_query=' + query + '&start=' + str(start) + '&max_results=100&sortBy=lastUpdatedDate&sortOrder=descending'
        data = requests.get(url).text 
        entries = parse(data, "entry")
        for entry in entries:
            url = parse(entry,"id")[0]
            if not(url in ids):
                title = parse(entry, "title")[0]
                date = parse(entry, "published")[0]
                message = "\n".join(["=" * 10 , "No." + str(counter + 1), "Title: " + title, "URL: " + url, "Published: " + date])
                requests.post(api_url, json={"text":message})
                ids.append(url)
                counter += 1
                if counter == 10:
                    return 0
            
            if counter == 0 and len(entries) < 100:
                requests.post(api_url, json={"text": "Currently, there is no available papers"})
                return 0
            elif counter == 0 and len(entries) == 100:
                start += 100

if __name__ == "__main__":
    print("Publish")
    api_url = "YOUR_URL"
    if os.path.exists("published.pkl"):
        with open("published.pkl",'rb') as web:
            ids = pickle.load(web)
    else:
        ids = []
    query = "(cat:start.ML + OR + cat:cs.CV + OR + cs.HR + OR + cs.IR) + AND + ((abs:word1)+OR+(abs:word2)+OR+(abs:word3)+OR+(abs:word4)+OR+(abs:word5))"
    start = 0
    requests.post(api_url, json={"text":"Hello!!"})
    serch_and_send(query, start, ids, api_url)
    pickle.dump(ids, open("published.pkl","wb"))