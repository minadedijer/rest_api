from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

users = {
    'users_list':
    [
        {
            'id': 'xyz789',
            'name': 'Charlie',
            'job': 'Janitor',
        },
        {
            'id': 'abc123',
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id': 'ppp222',
            'name': 'Mac',
            'job': 'Professor',
        },
        {
            'id': 'yat999',
            'name': 'Dee',
            'job': 'Actress',
        },
        {
            'id': 'for219',
            'name': 'Doo',
            'job': 'Actress',
        },
        {
            'id': 'zap555',
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}


@app.route('/users/<user_id>', methods=['GET', 'DELETE'])
def get_user(user_id):
    if request.method == 'GET':
        for user in users['users_list']:
            if user_id == user['id']:
                return user
        return jsonify(success=False, status=404)
    elif request.method == 'DELETE':
        to_delete = None
        for i, user in enumerate(users['users_list']):
            if user_id == user['id']:
                del users['users_list'][i]
                return jsonify(success=True)

        return make_response(jsonify(success=False), 404)


def name_filter(name):
    return lambda x: x['name'] == name


def job_filter(job):
    return lambda x: x['job'] == job


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        query = users['users_list']

        search_username = request.args.get('name')
        if search_username:
            query = filter(name_filter(search_username), query)

        search_job = request.args.get('job')
        if search_job:
            query = filter(job_filter(search_job), query)

        return jsonify(list(query))
    elif request.method == 'POST':
        userToAdd = request.get_json()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        return resp
    raise Exception("Unsupported method")


@app.route('/')
def hello_world():
    return 'Hello, world!'
