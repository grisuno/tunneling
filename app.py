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

app = Flask(__name__)

@app.route('/')
def home():
    url = request.args.get('url')
    if url:
        return f'<iframe src="/proxy?url={url}" width="100%" height="600px"></iframe>'
    return 'Please provide a URL as a query parameter.'

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}", 500

    content_type = response.headers.get('Content-Type', '')

    if 'text/html' in content_type:
        return render_template_string(response.text)
    else:
        return Response(response.content, content_type=content_type)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
