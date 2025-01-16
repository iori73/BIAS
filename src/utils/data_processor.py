import re

def extract_guest_name(description):
    pattern = r'ゲスト・(.+?)さん'
    match = re.search(pattern, description)
    return match.group(1) if match else None

def extract_university(description):
    pattern = r'([\w\s]+大学[\w\s]+学部[\w\s]+学科|[\w\s]+大学[\w\s]+学部)'
    match = re.search(pattern, description)
    return match.group(1) if match else None

def extract_grad_school(description):
    pattern = r'([\w\s]+大学院[\w\s]+研究科)'
    match = re.search(pattern, description)
    return match.group(1) if match else None

def extract_employer(description):
    # 現在の勤務先を抽出するパターン
    patterns = [
        r'現在は([\w\s]+)で',
        r'([\w\s]+)に就職',
        r'([\w\s]+)で勤務'
    ]
    for pattern in patterns:
        match = re.search(pattern, description)
        if match:
            return match.group(1)
    return None
