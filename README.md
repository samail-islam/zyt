# zyt 🧩  
*A simple GitHub repository manager from the terminal*

---

## About

**zyt** is a lightweight command-line tool that simplifies common GitHub workflows such as cloning, forking, updating, syncing, and managing repositories.  
It acts as a small wrapper around `git`, `ssh`, and (optionally) the GitHub CLI (`gh`) to reduce repetitive commands and decision-making.

The goal of **zyt** is to let you work with repositories using **short, memorable commands** while automatically choosing the best authentication method available.

---

## The Problem It Solves

Working with GitHub repositories often involves:

- Remembering long `git` commands
- Manually setting `upstream` for forks
- Handling SSH vs HTTPS vs GitHub CLI
- Keeping forks up-to-date with upstream
- Cloning private repositories reliably

**zyt** solves these by:

- Auto-detecting authentication (GitHub CLI → SSH → HTTPS)
- Automatically configuring `origin` and `upstream`
- Providing one-command workflows for common tasks
- Reducing setup friction for contributors

---

## Features

- 📥 Clone public and private repositories
- 🍴 Fork repositories with upstream automatically configured
- 🔄 Sync forks with upstream (rebase → merge fallback)
- ⬆️ Update repositories safely
- 🗑️ Uninstall cloned repositories
- 🔐 Authentication auto-detection
- ⚙️ Minimal dependencies 

---

## Requirements

- Python **3.7+**
- `git`
- One of the following for authentication:
  - **GitHub CLI (`gh`)** *(recommended)*
  - **SSH key configured with GitHub**
  - **HTTPS credentials / token**

Optional but recommended:
- `gh` authenticated via:
  ```bash
  gh auth login

## Getting started

- Clone this  repository:
	```bash
	git clone https://github.com/samail-islam/zyt.git
	```
- Setup zyt:
	- For bash (Linux-based/MacOS):
		```bash
		cd zyt && bash setup.sh
		```
  This will automatically setup the `zyt` command to work on any directory and delete the powershell script.
	
	- For powershell (Windows):
		```powershell
		
		```
  This will automatically setup the `zyt` command to work on any directory and delete the bash script.

   >`zyt` hasn't yet tested on Windows,if any error   occurs, please notify by creating an issue or start a pull request.
     
     
## Usage

```bash
zyt <command> <username/repository>
```
- Commands
  - clone a repository
    ```bash
    zyt in <username/repository>
    ```
    - Works for public repositories
    - Works for private repositories if authenticated

  - delete a repository
    ```bash
    zyt <command> <username/repository>
    ```
    - Removes the local directory after confirmation

  - update a repository
    ```bash
    zyt <command> <username/repository>
    ```
    - Deletes old local copy
    - Clones a fresh copy
    - Useful for corrupted or outdated directories
    - works if on the 
```bash
zyt <command> <username/repository>
``` ```bash
zyt <command> <username/repository>
```
  
  
