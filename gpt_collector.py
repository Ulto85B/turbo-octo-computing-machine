from github import Github


git_user = Github("Ulto85B",TOKEN)
import os
from github import Github
my_secret = os.environ['PASSWORD']
g_user = Github("Ulto85B",my_secret)
result = g_user.search_repositories("pygame")
for repo in result:
  os.system(f'git clone {repo} git_files')

