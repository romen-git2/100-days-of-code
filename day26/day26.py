import sqlite3
import requests
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

# data structure
@dataclass
class GitHubProfile:
    username: str
    name: Optional[str]
    bio: Optional[str]
    public_repos: int
    followers: int
    last_updated: str

# database layer
class DatabaseManager:
    def __init__(self, db_name="agent_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS github_profiles (
                username TEXT PRIMARY KEY,
                name TEXT,
                bio TEXT,
                public_repos INTEGER,
                followers INTEGER,
                fetched_at TIMESTAMP
            )
        ''')
        self.conn.commit()

    def save_profile(self, profile: GitHubProfile):
        """Insert new or Update existing"""
        print(f"Saving profile for {profile.username}...")
        self.cursor.execute('''
            INSERT INTO github_profiles VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(username) DO UPDATE SET
                name=excluded.name,
                bio=excluded.bio,
                public_repos=excluded.public_repos,
                followers=excluded.followers,
                fetched_at=excluded.fetched_at
        ''', (
            profile.username, profile.name, profile.bio, 
            profile.public_repos, profile.followers, profile.last_updated
        ))
        self.conn.commit()

    def get_stats(self):
        self.cursor.execute("SELECT COUNT(*) FROM github_profiles")
        return self.cursor.fetchone()[0]

    def close(self):
        self.conn.close()

# API layer
class GitHubAPI:
    BASE_URL = "https://api.github.com/users"

    def fetch_user(self, username: str) -> Optional[GitHubProfile]:
        print(f"Fetching data for {username}...")
        try:
            response = requests.get(f"{self.BASE_URL}/{username}")
            if response.status_code == 404:
                print(f"User {username} not found.")
                return None
            
            data = response.json()
            return GitHubProfile(
                username=data['login'],
                name=data.get('name'),
                bio=data.get('bio'),
                public_repos=data['public_repos'],
                followers=data['followers'],
                last_updated=datetime.now().isoformat()
            )
        except Exception as e:
            print(f"Network issue: {e}")
            return None

# agent tool(coordinator)
class AgentTool:
    def __init__(self):
        self.db = DatabaseManager()
        self.api = GitHubAPI()

    def analyze_user(self, username):
        # fetch
        profile = self.api.fetch_user(username)
        
        if profile:
            # logic/process(print for now)
            print(f"Found {profile.name} | Repos: {profile.public_repos} | Followers: {profile.followers}")
            
            # store
            self.db.save_profile(profile)
        else:
            print("Skipping database save.")

    def close(self):
        print(f"Total profiles in DB: {self.db.get_stats()}")
        self.db.close()

if __name__ == "__main__":
    tool = AgentTool()
    
    targets = ["torvalds", "romen-git", "romen-git2", "defunkt"]
    
    print("Starting Agent Tool Run")
    for target in targets:
        tool.analyze_user(target)
    
    tool.close()
    print("Run Complete")