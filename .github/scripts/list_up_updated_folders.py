import subprocess
import os
import json
from pathlib import Path

BASE_DIR = Path("dockerfiles")

# Get the modified files in the last commit
diff_output = subprocess.check_output(["git", "diff", "--name-only", "HEAD^...HEAD"], text=True)
print("Changed files:", diff_output.strip())
changed_files = diff_output.strip().splitlines()

# Get the folder names
changed_dirs = {
    Path(f).parts[1]
    for f in changed_files
    if f.startswith(f"{BASE_DIR}/") and len(Path(f).parts) > 1
}
changed_dirs = [d for d in changed_dirs 
                if (BASE_DIR/d).exists() and (BASE_DIR/d).is_dir()]
# Export the JSON output for GitHub Actions

def get_dir_info(directory):
    dir_path = BASE_DIR / directory
    tag = (dir_path/"version").read_text().strip() if (dir_path/"version").exists() else "latest"
    return {
        "directory": dir_path,
        "name": directory,
        "tag":tag,
    }

matrix = [get_dir_info(d) for d in sorted(changed_dirs)]
print(matrix)
with open(os.environ["GITHUB_OUTPUT"], "w") as f:
    f.write(f"matrix={json.dumps(matrix)}\n")