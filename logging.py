class LogSystem:
    def __init__(self, capacity):
        self.capacity = capacity            
        self.recent_logs = []              
        self.user_logs = {}                
        self.level_count = {}             

    def add_log(self, line):
        parts = line.split(" ", 3)
        timestamp = parts[0][1:-1]       
        level = parts[1]                   
        user_part = parts[2].split(":")
        user_id = user_part[0]             
        message = user_part[1].strip() if len(user_part) > 1 else parts[3].strip()

        log = {
            "timestamp": timestamp,
            "level": level,
            "user_id": user_id,
            "message": message
        }

        self.recent_logs.append(log)
        if len(self.recent_logs) > self.capacity:
            self.recent_logs.pop(0)

        if user_id not in self.user_logs:
            self.user_logs[user_id] = []
        self.user_logs[user_id].append(log)

        if level not in self.level_count:
            self.level_count[level] = 0
        self.level_count[level] += 1

    def get_user_logs(self, user_id):
        return self.user_logs.get(user_id, [])

    def count_levels(self):
        return self.level_count

    def filter_logs(self, keyword):
        keyword = keyword.lower()
        result = []
        for log in self.recent_logs:
            if keyword in log["message"].lower():
                result.append(log)
        return result

    def get_recent_logs(self):
        return self.recent_logs


def main():
    log_system = LogSystem(5)

    logs = [
        "[2023-10-01 12:00:00] INFO user1: User logged in",
        "[2023-10-01 12:05:00] ERROR user2: Failed to load resource",
        "[2023-10-01 12:10:00] INFO user1: User updated profile",
        "[2023-10-01 12:15:00] WARNING user3: Low disk space",
        "[2023-10-01 12:20:00] INFO user2: User logged out"
    ]

    for log in logs:
        log_system.add_log(log)

    print("Recent Logs:", log_system.get_recent_logs())
    print("User Logs for user1:", log_system.get_user_logs("user1"))
    print("Level Counts:", log_system.count_levels())
    print("Filtered Logs containing 'user':", log_system.filter_logs("user"))
if __name__ == "__main__":
    main()
    
