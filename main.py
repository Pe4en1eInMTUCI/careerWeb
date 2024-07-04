import requests
from flask import Flask, request, render_template
import requests as rq

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/search')
def search():
    job = request.args.get("job")


    data = requests.get(f"http://127.0.0.1:8800/getVacancies?name={job}").json()


    return render_template('search.html', job=job, vacancies=data)

if __name__ == '__main__':
    app.run(debug=True, port=80)