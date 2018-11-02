import subprocess
import json
import os
import sys

def res_cmd(cmd):
    return subprocess.Popen(
            cmd, stdout=subprocess.PIPE,
            shell=True).communicate()[0]

def all_repo_clone(target, org, page):
    if not res_cmd('echo $GITHUB_TOKEN').strip():
        token = input('Github token : ')
        os.system(f"export $GITHUB_TOKEN=\"{token}\"")
    if not os.path.exists(f"{org}"):
        os.mkdir(f"{org}")
    cmd = f"curl -s https://$GITHUB_TOKEN:@api.github.com/{target}/{org}/repos\?per_page\=100\&page={page}"
    res = json.loads(res_cmd(cmd))
    for r in res:
        os.system(f"cd {org} && git clone {r['html_url']}")
        print()

def all_repo_pull(dir_path):
    for d in filter(lambda x: os.path.isdir(x), os.listdir(dir_path)):
        print(d)
        os.system(f"cd {d} && git pull")
        print()
