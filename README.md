# issues_to_csv
## Requirements
- Python 2.x
- requests (==2.5.3)

## Usage
Please just Simply follow the interactive console and carefully provide required information.
```
$ python issues_to_csv.py
  username: (ex. keiichirosoeda)
  password: ********
  repo (username/repo): (ex. keiichirosoeda/issues_to_csv)
  state ("open", "closed", "all", default=all): (ex. open)
```

If typing those things bothers you, just replace `github_user`, `github_password`, `repo` and `state` like this:
```
github_user = 'keiichirosoeda'
github_password = '********'
repo = 'keiichirosoeda/issues_to_csv'
state = 'all'
```
so that it won't ask you for information anymore.
