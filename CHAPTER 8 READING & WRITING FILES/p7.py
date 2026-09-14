#write_report(filename, lines) — takes a list of strings and writes them to a 
#new file, one per line. Use mode 'w'. Run it twice on the same file and 
# check what happened to the old content.

def write_report(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

write_report("report.txt",["Hello, Aman, Yadav"])

write_report("report.txt",["Yadav, Aman, Hello"])

with open('report.txt','r') as f:
          print(f.read())

