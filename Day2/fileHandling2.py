from collections import defaultdict, deque

logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]

# Data structures
User_Dict = defaultdict(list)
level_Dict = defaultdict(int)
recent_logs = deque(maxlen=5)
parsed_logs = []  # All parsed logs to save in text file

# Decorator to parse log strings
def parse_log(func):
    def wrapper(log_line: str):
        arr = log_line.split(" ", 3)
        timestamp = arr[0].strip("[]")
        level = arr[1]
        user = arr[2].split(":")[0]
        message = arr[3]
        log_dict = {
            "timestamp": timestamp,
            "level": level,
            "user": user,
            "message": message.strip()
        }
        return func(log_dict)
    return wrapper

# Decorated add_log function
@parse_log
def add_log(log: dict):
    parsed_logs.append(log)
    recent_logs.append(log)
    User_Dict[log["user"]].append(log)
    level_Dict[log["level"]] += 1

# Process all logs
for entry in logs:
    add_log(entry)

# Save to logs.txt in a readable format
with open("logs.txt", "w") as f:
    for log in parsed_logs:
        line = f"[{log['timestamp']}] {log['level']} {log['user']}: {log['message']}\n"
        f.write(line)

print("Parsed logs saved to logs.txt ✅")
