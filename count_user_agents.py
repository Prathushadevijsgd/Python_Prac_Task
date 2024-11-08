import sys
import re
from collections import Counter

def extract_user_agent(log_line):
    user_agent_pattern = r'".*?"\s+"(.*?)"$'
    match = re.search(user_agent_pattern, log_line)
    if match:
        return match.group(1)
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    
    user_agents_counter = Counter()
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                user_agent = extract_user_agent(line)
                if user_agent:
                    user_agents_counter[user_agent] += 1
        
        print(f"Total number of unique User Agents: {len(user_agents_counter)}")
        
        for user_agent, count in user_agents_counter.items():
            print(f"{user_agent}: {count} requests")
    
    except FileNotFoundError:
        print(f"Error: The file '{log_file}' was not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
