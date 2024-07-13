from flask import Flask, request, jsonify, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/', methods=['GET'])
def submit_login():
    with open('logins.csv', 'a', newline='') as csvfile:
        fieldnames = ['timestamp', 'remote_addr', 'user_agent', 'url', 'method']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()
 
        writer.writerow({
            'timestamp': request.environ.get('REQUEST_TIME'),
            'remote_addr': request.remote_addr,
            'user_agent': request.headers.get('User-Agent'),
            'url': request.url,
            'method': request.method
        })

    return redirect('https://www.youtube.com/watch?v=BBJa32lCaaY&ab_channel=LegacyPNDA')

if __name__ == '__main__':
    app.run(debug=True)
