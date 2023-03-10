# Git Repository Manage Helper Tools

These scripts have been created to make it easier to manage git repositories, and to detect currently used repositories

## First step

In order to use these tools you have to install [python](https://www.python.org/downloads/) 3.* (recommended 3.9)

Clone this repository

```commandline
git clone https://github.com/nurefexc/git_repo_helper.git
```

And is done

## List Repositories

List all git repositories on the machine

```commandline
python list_repositories.py
```

Search git repositories in specified directories and subdirectories

```commandline
python list_repositories.py C:\work C:\hobby_project
```