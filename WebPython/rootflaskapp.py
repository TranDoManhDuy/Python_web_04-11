from flask import Flask, render_template, redirect, url_for, jsonify, request, abort, send_from_directory
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'WebPython/static'