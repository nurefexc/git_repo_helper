import os
import string
import sys
from time import time

def list_all_of_repository(path):
    """
    Searches all presumably git repositories in the specified directory and its subfolders
    :param path: Directory location
    :return: Git repositories location
    """
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == ".git":
                yield root


if __name__ == '__main__':
    # Log start time
    start = time()

    # Git repository locations
    all_of_repositories = []

    # Location of start search dictionory
    locations = []

    # If an initial search directories is specified, search there, if not, search the entire machine
    if len(sys.argv) > 1:
        locations = sys.argv[1:]
    else:
        locations = ['%s:\\' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

    # Search '.git' dictionary and write screen
    for location in locations:
        if os.path.exists(location):
            for repository in list_all_of_repository(f"{location}"):
                all_of_repositories.append(repository)
                print(repository)

    # Log end time
    end = time()

    # Write screen statistic information
    if all_of_repositories:
        print(f"\nTotal git repositories number: {len(all_of_repositories)}")
    else:
        print("Sorry I could not find git repository")
    print(f"The time of execution of above program is : {int(end - start)}s")

    # Warning message if has doesnt exist location
    for location in locations:
        if not os.path.exists(location):
            print(f"\nWarning: The {location} path cannot be found")