from abc import ABC, abstractmethod
import time

# command interface
class Command(ABC):
    """
    The interface that all commands must follow
    """
    @abstractmethod
    def execute(self):
        pass

# concrete commands
class SaveFileCommand(Command):
    def __init__(self, filename: str, content: str):
        self.filename = filename
        self.content = content

    def execute(self):
        print(f"Saving to '{self.filename}': {self.content}...")
        # simulate file I/O
        time.sleep(0.5)

class EmailCommand(Command):
    def __init__(self, recipient: str, subject: str):
        self.recipient = recipient
        self.subject = subject

    def execute(self):
        print(f"Sending email to {self.recipient}. Subject='{self.subject}'")
        time.sleep(0.5)

# invoker (agent executor)
class AgentExecutor:
    def __init__(self):
        self._command_queue = []
        self._history = []

    def add_command(self, command: Command):
        """Adds a command to the plan (queue)"""
        print(f"Added {command.__class__.__name__} to queue.")
        self._command_queue.append(command)

    def execute_pending(self):
        """Runs all queued commands"""
        print(f"Executing Plan ({len(self._command_queue)} steps)")
        
        while self._command_queue:
            command = self._command_queue.pop(0)
            try:
                command.execute()
                self._history.append(command)
            except Exception as e:
                print(f"Error executing command: {e}")
                
        print("Plan Complete")

    def show_history(self):
        print(f"Execution History: {[cmd.__class__.__name__ for cmd in self._history]}")

if __name__ == "__main__":
    # invoker
    executor = AgentExecutor()

    # the agent planning phase (creating objects, not running them yet)
    print("Agent is thinking and building a plan...")
    cmd1 = SaveFileCommand("report.txt", "Analysis of financial data...")
    cmd2 = EmailCommand("admin@corp.com", "Report Ready")
    cmd3 = SaveFileCommand("log.txt", "Email sent successfully.")

    # queueing the commands
    executor.add_command(cmd1)
    executor.add_command(cmd2)
    executor.add_command(cmd3)

    # the agent action phase
    executor.execute_pending()
    
    # verify history
    executor.show_history()