import sqlite3
from datetime import datetime

class AgentMemory:
    def __init__(self, db_name="agent_memory.db"):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        """Create the database and table if they don't exist"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS agent_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    agent_name TEXT,
                    task TEXT,
                    result TEXT
                )
            ''')
            conn.commit()

    def commit_to_memory(self, agent_name, task, result):
        """Save a new interaction to the database"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO agent_logs (timestamp, agent_name, task, result)
                VALUES (?, ?, ?, ?)
            ''', (timestamp, agent_name, task, result))
            conn.commit()
        print(f"Logged: {task}")

    def recall_all(self):
        """Retrieve all stored memories"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM agent_logs ORDER BY timestamp DESC")
            return cursor.fetchall()

if __name__ == "__main__":
    # initialize the memory
    memory = AgentMemory()

    print("Agent is performing tasks...")
    memory.commit_to_memory("Spotify Agent", "Fetched Top 50 Chart", "SUCCESS")
    memory.commit_to_memory("Webhook Agent", "Received Alert", "ACTION_TAKEN")
    
    print("Agent's Long-Term History:")
    history = memory.recall_all()
    
    for entry in history:
        print(f"[{entry[1]}] {entry[2]} performed '{entry[3]}' -> Status: {entry[4]}")