import functions as cmd
import sys
# ---- Command map ----
COMMANDS = {
    "in": lambda repo, url: cmd.install(url),
    "un": lambda repo, url: cmd.uninstall(repo),
    "up": lambda repo, url: cmd.update(repo, url),
    "f":  lambda repo, url: cmd.fork(repo),
    "sync": lambda repo, url: cmd.sync(repo)
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
