import os.path
import sys
import requests
from collections import namedtuple
from .envs import API_KEY, USER_NAME

Kata = namedtuple('Kata', 'name url slug rank description')

# language = 'python'

access_key = API_KEY

def get_kata_data(slug, access_key):
    url = 'https://www.codewars.com/api/v1/code-challenges/%s' % slug
    params = {'access_key': access_key}
    response = requests.get(url, params)

    if response.status_code != 200:
        sys.stdout.write('ERROR\n')
        raise ValueError('Can not retrieve kata data from the server!')
    else:
        return response.json()
        

def process_kata_data(data):
    """Convert raw kata data into manageable namedtuple
    Args:
        data {dict}: Converted to dict json data from response
    Returns:
        namedtuple: Kata(name, url, slug, rank, description)
    """
    name = data['name']
    url = data['url']
    slug = data['slug']
    rank = str(abs(data['rank']['id']))
    description = data['description']
    return Kata(name, url, slug, rank, description)


def create_file(data, file_type):
    if file_type == 'solution':
        filename = data.slug.replace('-', '_') + '.py'
        directory = os.path.join('solutions', 'kyu_' + data.rank)
        full_path = os.path.join(directory, filename)
    elif file_type == 'test':
        filename = 'test_' + data.slug.replace('-', '_') + '.py'
        directory = os.path.join('tests', 'solutions', 'kyu_' + data.rank)
        full_path = os.path.join(directory, filename)
    else:
        raise ValueError('Unknown file type')

    if not os.path.isdir(directory):
        os.makedirs(directory)

    if not os.path.isfile(full_path):
        with open(full_path, 'w') as file:
            pass


def create_solution_file(data):
    create_file(data, 'solution')


def create_test_file(data):
    create_file(data, 'test')
    
    
def new_solution(slug):
    """Create new solution template"""
    sys.stdout.write('Get kata data...')
    data = get_kata_data(slug, access_key)
    sys.stdout.write('DONE\n')

    sys.stdout.write('Process data...'),
    data = process_kata_data(data)
    sys.stdout.write('DONE\n')

    sys.stdout.write('Create solution file...')
    create_solution_file(data)
    sys.stdout.write('DONE\n')

    sys.stdout.write('Create test file...')
    create_test_file(data)
    sys.stdout.write('DONE\n')