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

# Export the JSON output for GitHub Actions

def get_dir_info(directory):
    """ディレクトリの情報を取得する関数"""
    dir_path = BASE_DIR / directory
    return {
        "directory": directory,
        "dockerfile": str(dir_path / "Dockerfile"),
        "context": str(dir_path),
    }

matrix = [get_dir_info(d) for d in sorted(changed_dirs)]
with open(os.environ["GITHUB_OUTPUT"], "w") as f:
    f.write(f"matrix={json.dumps(matrix)}\n")