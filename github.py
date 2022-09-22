from git import Repo
import git
import os

def importacaoGit():
    path = 'dep'
    Repo.clone_from("https://github.com/nairamouras/teste-instaview-dep", path)
    return

def exclusaoRepo(path):
    if os.path.exists(path):
        git.rmtree(path)
    return
    
