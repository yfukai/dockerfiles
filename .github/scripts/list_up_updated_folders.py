import subprocess
import os
import json
from pathlib import Path

BASE_DIR = Path("some_root")

# 差分ファイルの一覧を取得
diff_output = subprocess.check_output(["git", "diff", "--name-only", "origin/main...HEAD"], text=True)
changed_files = diff_output.strip().splitlines()

# BASE_DIR 配下のサブディレクトリ名を取得
changed_dirs = {
    Path(f).parts[1]
    for f in changed_files
    if f.startswith(f"{BASE_DIR}/") and len(Path(f).parts) > 1
}

# matrix 用の JSON 出力
matrix = [{"dir": d} for d in sorted(changed_dirs)]
with open(os.environ["GITHUB_OUTPUT"], "w") as f:
    f.write(f"matrix={json.dumps(matrix)}\n")