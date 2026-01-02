#!/usr/bin/env python3
import sys
import os
import shutil
import subprocess


def install(url):
    subprocess.run(["git", "clone", url])

def uninstall(repo):
    if os.path.isdir(repo):
        consent = input(f"Are you sure you want to uninstall {repo}? (Y/n): ")
        if consent == "Y":
            shutil.rmtree(repo)
        else:
            print("Cancelled")
    else:
        print(f"No directory named {repo}")

def update(repo, url):
    # repo comes as "username/reponame"
    repo_name = repo.strip().split("/")[1]

    if os.path.isdir(repo_name):
        consent = input(f"Are you sure you want to update {repo}?\n (updating will delete all old data)? (Y/n): ")
        if consent == "Y":
            #rename directory before cloning to avoid conflict 
            trash_dir = repo_name + "_trash" 
            os.rename(repo_name, trash_dir)
            subprocess.run(["git", "clone", url])
            #delete directory if cloning successful 
            shutil.rmtree(trash_dir)
        else:
            print("Cancelled")
    else:
        print(f"No directory named {repo_name}")
def detect_auth_method():
    """
    Returns: 'gh', 'ssh', or 'https'
    """
    def has_cmd(cmd):
        return shutil.which(cmd) is not None
    if has_cmd("gh"):
        try:
            subprocess.run(
                ["gh", "auth", "status"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
            return "gh"
        except subprocess.CalledProcessError:
            pass
    try:
        subprocess.run(
            ["ssh", "-T", "git@github.com"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5
        )
        return "ssh"
    except Exception:
        pass
    
    return "https"

def sync(repo):
    repo_name = repo.split("/")[1]

    if not os.path.isdir(repo_name):
        print("Repository not found locally")
        return

    os.chdir(repo_name)
    subprocess.run(["git", "fetch", "upstream"])

    # detect branch
    branch = subprocess.check_output(["git", "branch", "--show-current"],text=True).strip()

    # try rebase first, fallback to merge
    result = subprocess.run(["git", "rebase", f"upstream/{branch}"])

    if result.returncode != 0:
        print("Rebase failed, falling back to merge")
        subprocess.run(["git", "rebase", "--abort"])
        subprocess.run(["git", "merge", f"upstream/{branch}"])

def fork(repo):
    user, repo_name = repo.split("/")
    method = detect_auth_method()

    if method == "gh":
        subprocess.run(["gh", "repo", "fork", repo, "--clone"])
        os.chdir(repo_name)
        subprocess.run([
            "git", "remote", "add",
            "upstream",
            f"https://github.com/{user}/{repo_name}.git"
        ])
        return

    # No gh → clone original + set upstream
    if method == "ssh":
        url = f"git@github.com:{user}/{repo_name}.git"
    else:
        url = f"https://github.com/{user}/{repo_name}.git"

    subprocess.run(["git", "clone", url])
    os.chdir(repo_name)
    subprocess.run(["git", "remote", "add", "upstream", url])


# ---- Command map ----
COMMANDS = {
    "in": lambda repo, url: install(url),
    "un": lambda repo, url: uninstall(repo),
    "up": lambda repo, url: update(repo, url),
    "f":  lambda repo, url: fork(repo),
    "sync": lambda repo, url: sync(repo)
}



def handle_command(command, repo):
    if command not in COMMANDS:
        print("Unknown command")
        sys.exit(1)

    url = "https://github.com/" + repo
    COMMANDS[command](repo, url)

def main():
    if len(sys.argv) != 3:
        print(
            """Usage:
              zyt in <username/reponame>  - clone a repo
              zyt un <reponame>           - delete a cloned repo
              zyt up <username/reponame>  - update a cloned repo
              zyt f <username/reponame>   - fork a repo
              zyt sync <username/reponame>- to fetch+ rebase upstream"""
              )
        sys.exit(1)

    command = sys.argv[1]
    repo = sys.argv[2]
    handle_command(command, repo)


if __name__ == "__main__":
    try:
    	main()
    except Exception as e:
    	print(e)
