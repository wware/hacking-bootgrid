from flask import Flask, request, render_template, send_from_directory, jsonify
import os
import random
import yaml

app = Flask(__name__)

with open("movies.yml", 'rU') as yamlfile:
    movies = yaml.load(yamlfile.read())

ratings = (
    "Lame",
    "Good",
    "Awesome",
    "Insanely awesome",
    "Life changing"
)

_id = 1
for m in movies:
    m["rating_imdb"] = ratings[random.randint(0, len(ratings) - 1)]
    m["id"] = _id
    _id += 1


@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/getdata', methods=['POST'])
def fetch_data():
    current = int(request.form.get('current'))
    rowCount = int(request.form.get('rowCount'))
    items = movies[:]
    dct = {}
    for k in request.form.keys():
        dct[k] = request.form.get(k)
    def has_term(item, s=request.form.get('searchPhrase')):
        return (
            (not s) or
            s.lower() in str(item['year']) or
            s.lower() in item['movie'].lower() or
            s.lower() in item['genre'].lower() or
            s.lower() in item['rating_imdb'].lower()
        )
    items = filter(has_term, items)
    for thing in ('id', 'movie', 'year', 'genre', 'rating_imdb'):
        def sortfunc(x, y, thing=thing):
            return cmp(x[thing], y[thing])
        key = 'sort[{0}]'.format(thing)
        if dct.get(key) == 'asc':
            items.sort(sortfunc)
        elif dct.get(key) == 'desc':
            def reverse(x, y, func=sortfunc):
                return func(y, x)
            items.sort(reverse)
    a, b = (current - 1) * rowCount, current * rowCount
    return jsonify({
        'current': current,
        'rows': items[a:min(b,len(items))],
        'rowCount': min(b,len(items)) - a,
        'total': len(items)
    })


@app.route('/js/<path:path>')
def send_js(path):
    path = os.path.join('js', path)
    return app.send_static_file(path)


@app.route('/css/<path:path>')
def send_css(path):
    path = os.path.join('css', path)
    return app.send_static_file(path)


@app.route('/fonts/<path:path>')
def send_fonts(path):
    path = os.path.join('fonts', path)
    return app.send_static_file(path)


if __name__ == '__main__':
    app.debug = True
    app.run()
