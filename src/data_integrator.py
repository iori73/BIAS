# # src/data_integrator.py
# import pandas as pd
# import os
# from utils.repo_manager import clone_podcast_notes

# def read_episode_summary(episode_title):
#     repo_path = clone_podcast_notes()
#     summary_path = os.path.join(repo_path, 'outputs', episode_title, 'episode_summary.md')
    
#     try:
#         if os.path.exists(summary_path):
#             with open(summary_path, 'r', encoding='utf-8') as f:
#                 return f.read()
#     except Exception as e:
#         print(f"Error reading summary for {episode_title}: {e}")
#     return None

# def update_csv_with_summaries(csv_path):
#     df = pd.read_csv(csv_path)
    
#     for index, row in df.iterrows():
#         if pd.isna(row['country']) or pd.isna(row['Current Employer']):
#             summary = read_episode_summary(row['Episode title'])
#             if summary:
#                 # 情報抽出ロジックを実装
#                 pass
    
#     return df


import os
import pandas as pd
import re

def read_episode_summary(episode_title):
    repo_path = os.path.join(os.getcwd(), "temp_podcast_notes")
    summary_path = os.path.join(repo_path, 'outputs', episode_title, 'episode_summary.md')
    
    try:
        if os.path.exists(summary_path):
            with open(summary_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            print(f"Summary file not found for: {episode_title}")
    except Exception as e:
        print(f"Error reading summary for {episode_title}: {e}")
    return None

def update_csv_with_summaries():
    # 絶対パスを使用
    csv_path = os.path.join(os.getcwd(), 'data', 'processed_episodes.csv')
    
    if not os.path.exists(csv_path):
        print(f"CSV file not found at: {csv_path}")
        return
        
    df = pd.read_csv(csv_path)
    updated = False
    
    for index, row in df.iterrows():
        if pd.isna(row['country']):
            summary = read_episode_summary(row['Episode title'])
            if summary:
                country = extract_location_info(summary)
                if country:
                    df.at[index, 'country'] = country
                    updated = True
                    print(f"Updated country for {row['Episode title']}: {country}")
    
    if updated:
        output_path = os.path.join(os.getcwd(), 'data', 'enriched_episodes.csv')
        df.to_csv(output_path, index=False)
        print(f"Saved enriched data to: {output_path}")
    else:
        print("No updates were made to the data")

if __name__ == "__main__":
    update_csv_with_summaries()
