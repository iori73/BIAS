# # src/utils/repo_manager.py
# import git
# import os

# def clone_podcast_notes():
#     repo_url = "https://github.com/iori73/podcast_notes_automation.git"
#     local_path = "./temp_podcast_notes"
    
#     if not os.path.exists(local_path):
#         git.Repo.clone_from(repo_url, local_path)
#     return local_path

import git
import os

def clone_podcast_notes():
    repo_url = "https://github.com/iori73/podcast_notes_automation.git"  # < >を削除
    local_path = os.path.join(os.getcwd(), "temp_podcast_notes")
    
    if not os.path.exists(local_path):
        try:
            git.Repo.clone_from(repo_url, local_path)
            print(f"Repository cloned successfully to {local_path}")
        except Exception as e:
            print(f"Error cloning repository: {e}")
    else:
        print(f"Repository already exists at {local_path}")
    
    return local_path
