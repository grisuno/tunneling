#!/usr/bin/env python3
# _*_ coding: utf8 _*_
"""
app.py

Autor: Gris Iscomeback
Correo electrónico: grisiscomeback[at]gmail[dot]com
Fecha de creación: 03/07/2024
Licencia: GPL v3

Descripción:  
"""
from flask import Flask, request, render_template_string, Response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url')
    if not url:
        return 'No URL provided', 400
    return render_template_string('<iframe src="/proxy?url={{ url }}" style="width:100%; height:100vh;"></iframe>', url=url)

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return 'No URL provided', 400
    response = requests.request(request.method, url, data=request.form)
    content_type = response.headers.get('Content-Type', '')

    if 'text/html' in content_type:
        soup = BeautifulSoup(response.content, 'html.parser')
        for tag in soup.find_all(['a', 'img', 'link', 'script']):
            attr = 'href' if tag.name == 'a' or tag.name == 'link' else 'src'
            if tag.has_attr(attr):
                original_url = tag[attr]
                if not original_url.startswith('http'):
                    original_url = requests.compat.urljoin(url, original_url)
                tag[attr] = f'/proxy?url={original_url}'
        html_content = str(soup)
        return Response(html_content, content_type=content_type)
    else:
        return Response(response.content, content_type=content_type)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
