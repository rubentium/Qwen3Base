from huggingface_hub import snapshot_download
import os

repo_id = "Qwen/Qwen3-0.6B-Base"  # Use the exact Repo ID
local_dir = "/mloscratch/homes/navasard/token_drop/qwen3_06b_base"

print(f"Starting download of {repo_id} to {local_dir}...")

snapshot_download(
    repo_id=repo_id,
    local_dir=local_dir,
    local_dir_use_symlinks=False, # Critical for local access
    token=True # Uses your logged-in token if the repo is gated
)

print("Download complete! Checking files...")
print(os.listdir(local_dir))