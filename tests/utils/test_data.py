import os
from datetime import datetime
# Get current date in YYYY-MM-DD format
today = datetime.now().strftime("%Y-%m-%d")

posts = [{"text": f"Post number {i}", "images": [], "tags": [], "location": ""} 
         for i in range(1, 5)
         ]

huddles = [
    {
        "eventName": f"Huddle {i} - {today}",
        "description": f"Description {i} - {today}"
    } 
    for i in range(1, 5)
]

test_posts = [
    {
        "text": "Plawright test post with photo and tags",
        "photo_path": "/Users/swatisalunkke/Downloads/Rafting2025/raft.jpeg",
        "location": "San jose, CA",
        "tags": ["tag1", "tag2"]
    }
]