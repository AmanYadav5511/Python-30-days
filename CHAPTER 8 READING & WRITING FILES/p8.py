#append_log_entry(filename, message) — 
# appends a single line to a log file using mode 'a', without erasing what's already there.
# Run it 3 times and confirm all 3 entries survive

def append_log_entry(filename, message):
    with open(filename, 'a') as f:
        f.write(message + '\n')

append_log_entry("log.txt", "First Entry")
append_log_entry("log.txt", "Second Entry")
append_log_entry("log.txt", "Third Entry")

with open('log.txt', 'r') as f:
    print(f.read())