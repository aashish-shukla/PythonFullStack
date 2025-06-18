from collections import defaultdict, deque

# Sample logs
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

# Decorator to parse log line string into dictionary
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

# Log processing function with decorator
@parse_log
def add_log(log: dict):
    user = log["user"]
    level = log["level"]
    recent_logs.append(log)
    User_Dict[user].append(log)
    level_Dict[level] += 1

# Feed logs
for entry in logs:
    add_log(entry)

# Print results
print("User Logs:")
print(dict(User_Dict))

print("\nLevel Counts:")
print(dict(level_Dict))

print("\nRecent Logs:")
print(list(recent_logs))
