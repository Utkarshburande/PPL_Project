src = input("Enter source file: ")
dest = input("Enter destination file: ")

with open(src, "r") as f:
    lines = f.readlines()

with open(dest, "w") as f:
    for line in lines:
        if not line.strip().startswith("#"):
            f.write(line)