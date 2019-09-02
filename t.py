import json
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash

def best_news():
    tweets = []
    with open('static/best_news.json', 'r') as json_file:
        data = json.load(json_file)
        return data
        # tweets.append(json.loads(line))
    #     print(json.loads(line))
    # return json.dumps([tweets])
    # return json.load(([json.loads(line) for line in open('static/best_news.json', 'r')]))

print(best_news())
