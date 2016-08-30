# coding: UTF-8
from getpass import getpass
import csv
import requests # 2.5.3

github_user = None
github_password = None
repo = None   # format is username/repo
state = None

GITHUB_USER = raw_input('username: ') if github_user is None else github_user
GITHUB_PASSWORD = getpass('password: ') if github_password is None else github_password
REPO = raw_input('repo ("username/repo"): ') if repo is None else repo
state = raw_input('state ("open", "closed", "all", default=all): ') if state is None else state
STATE = state if state is None else 'all'
print 'Exporting issues...'
ISSUES_FOR_REPO_URL = 'https://api.github.com/repos/%s/issues?state=%s' % (REPO, STATE)
AUTH = (GITHUB_USER, GITHUB_PASSWORD)

r = requests.get(ISSUES_FOR_REPO_URL, auth=AUTH)

filename = '%s-issues.csv' % (REPO.replace('/', '-'))
csvfile = open(filename, 'w')
writer = csv.writer(csvfile)
row = [
    'Number',
    'Id',
    'Title',
    'State',
    'Created by',
    'Asigned to',
    'Created at',
    'Updated at',
    'Closed at',
    'Milestone',
    'Labels',
    'Comments',
    'Body'
]
writer.writerow(row)

def write_issues(request):
    """issueの内容をcsvファイルに書き込む"""
    if not r.status_code == 200:
        raise Exception(r.status_code)
    for issue in r.json():

        if issue['assignee'] is None: issue['assignee'] = {'login': 'not assigned'}
        if issue['milestone'] is None: issue['milestone'] = {'title': ''}

        labels = []
        for label in issue['labels']:
            labels.append(label.encode('utf-8'))

        row = [
            issue['number'],
            issue['id'],
            issue['title'].encode('utf-8'),
            issue['state'].encode('utf-8'),
            issue['user']['login'].encode('utf-8'),
            issue['assignee']['login'].encode('utf-8'),
            issue['created_at'],
            issue['updated_at'],
            issue['closed_at'],
            issue['milestone']['title'].encode('utf-8'),
            '; '.join(labels),
            issue['comments'],
            issue['body'].encode('utf-8')
        ]
        writer.writerow(row)

def generate_links(request):
    """次のページのリンクを作成"""
    return dict(
        [(rel[6:-1], url[url.index('<')+1:-1]) for url, rel in
            [link.split(';') for link in
                r.headers['link'].split(',')]])

write_issues(r)

if 'link' in r.headers:
    links = generate_links(r)
    while 'last' in links and 'next' in links:
        r = requests.get(links['next'], auth=AUTH)
        write_issues(r)
        if links['next'] == links['last']:
            break
        links = generate_links(r)
