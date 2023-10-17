host_names = []
count = 0
host = input('From : ')
print(host)

file_name = "mbox.txt"
try:
    with open(file_name, "r") as file:
        for line in file:
            if line.startswith("From: " + host):
                email = line.split()[1]
                host_name = email.split("@")[1]
                host_names.append(host_name)
                count += 1
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
    exit()

for host in host_names:
    print(host)

print(f"Total {count} hosts printed")

