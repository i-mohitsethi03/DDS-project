from collections import deque
import time

class ChatHistoryManager:
    def __init__(self):
        # A deque (double-ended queue) to simulate the incoming message queue
        self.message_queue = deque()
        # A list acting as a stack for undo actions
        self.sent_messages = []
        # A list acting as a stack for redo actions
        self.undone_messages = []

    def send_message(self, message):
        """Adds a new message to the queue and moves it to the sent history."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        full_message = {"text": message, "timestamp": timestamp}
        self.message_queue.append(full_message)
        print(f"Message '{message}' queued at {timestamp}.")
        self.process_queue()

    def process_queue(self):
        """Processes the queue by moving messages to the sent history."""
        if self.message_queue:
            message = self.message_queue.popleft()
            self.sent_messages.append(message)
            print(f"Message '{message['text']}' sent at {message['timestamp']}.")
            # Clear the redo stack after a new message is sent
            self.undone_messages = []

    def undo_last_sent(self):
        """Moves the last sent message from the sent stack to the undone stack."""
        if not self.sent_messages:
            print("No messages to undo.")
            return

        last_message = self.sent_messages.pop()
        self.undone_messages.append(last_message)
        print(f"Undid message: '{last_message['text']}'")

    def redo_last_undone(self):
        """Moves the last undone message from the undone stack back to the sent stack."""
        if not self.undone_messages:
            print("No messages to redo.")
            return

        last_undone = self.undone_messages.pop()
        self.sent_messages.append(last_undone)
        print(f"Redid message: '{last_undone['text']}'")

    def show_history(self):
        """Displays the history of sent messages."""
        if not self.sent_messages:
            print("No messages in history.")
            return

        print("\n--- Message History ---")
        for i, msg in enumerate(self.sent_messages):
            print(f"{i+1}. [{msg['timestamp']}] {msg['text']}")
        print("-----------------------\n")

def main():
    manager = ChatHistoryManager()

    print("--- Chat History Manager ---")
    print("Commands:")
    print("  'send [message]' - sends a message")
    print("  'undo' - undoes the last sent message")
    print("  'redo' - redoes the last undone message")
    print("  'history' - shows all sent messages")
    print("  'exit' - quits the program")
    print("--------------------------\n")

    while True:
        user_input = input("Enter command: ").strip()
        if user_input.lower() == 'exit':
            break
        elif user_input.lower().startswith('send '):
            message_text = user_input[5:].strip()
            if message_text:
                manager.send_message(message_text)
            else:
                print("Message cannot be empty.")
        elif user_input.lower() == 'undo':
            manager.undo_last_sent()
        elif user_input.lower() == 'redo':
            manager.redo_last_undone()
        elif user_input.lower() == 'history':
            manager.show_history()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
