# issues_to_csv
Export github issues as a csv file.
## Requirements
- Python 2.x
- requests (==2.5.3)

## Usage
Just Simply follow the interactive console and carefully provide required information.
```
$ python issues_to_csv.py
  username: (ex. keiichirosoeda)
  password: (ex. ********)
  repo: (ex. keiichirosoeda/export_github_issues)
  state: (ex. open)
```

If typing those things bothers you, just modify the source code (replace `github_user`, `github_password`, `repo` and `state` with your own like this):
```
github_user = 'keiichirosoeda'
github_password = '********'
repo = 'keiichirosoeda/export_github_issues'
state = 'all'
```
so it won't ask you for information anymore.
