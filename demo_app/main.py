# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pathlib import Path
import datetime
import requests
import uvicorn
import logging
import base64
import csv
import os
import helpers


app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)
print(Path(__file__).parent.absolute() / "static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    data_file_path = '../datasets/paper_reader_demo/example_papers.csv'
    papers = []

    with open(data_file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            papers.append({
                'paper_name': row[0],
                'year': row[1],
                'title': row[2],
                'content': row[4],
                'num_of_words': len(row[4].split(' '))
            })

    return templates.TemplateResponse(
        "index.html",
        {
            'request': request,
            'papers': papers[1:]
        }
    )

if __name__ == '__main__':
    uvicorn.run(app, port=8081, host='0.0.0.0')
