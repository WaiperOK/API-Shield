from datetime import datetime

def log_and_store(log_messages, message):
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    log_entry = f"{timestamp} [INFO] {message.strip()}"
    log_messages.append(log_entry)
