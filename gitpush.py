import os
import subprocess

repo_path = "."   # repository path

def run(cmd):
    print("Running:", cmd)
    subprocess.run(cmd, shell=True, cwd=repo_path)

# get all files not yet tracked
result = subprocess.check_output(
    "git ls-files --others --exclude-standard",
    shell=True,
    cwd=repo_path
).decode().splitlines()

files = sorted(result)

print(f"Found {len(files)} files")

for f in files:
    print("\nProcessing:", f)

    run(f'git add "{f}"')
    run(f'git commit -m "Add {f}"')
    run("git push")

print("Done!")