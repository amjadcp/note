import os
import sys
from datetime import datetime
from diff_match_patch import diff_match_patch

# Configuration
INPUT_FILE = "sample.txt"      # File to track
DIFFS_DIR = "diffs"              # Directory to store diffs

def ensure_directory(path):
    """Create directory if it doesn't exist"""
    os.makedirs(path, exist_ok=True)

def read_file(path):
    """Read file content with proper encoding handling"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None

def write_file(path, content):
    """Write content to file with proper encoding"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def get_current_content():
    """Get current content of the input file"""
    return read_file(INPUT_FILE)

def create_base_version():
    """Create initial base version"""
    content = get_current_content()
    if content is None:
        print(f"Error: {INPUT_FILE} not found!")
        sys.exit(1)
        
    write_file(BASE_FILE, content)
    print(f"Created base version at {BASE_FILE}")

def get_diffs():
    """Get all stored diffs sorted by timestamp"""
    diffs = []
    if os.path.exists(DIFFS_DIR):
        diff_files = sorted(os.listdir(DIFFS_DIR))
        for df in diff_files:
            diffs.append(read_file(os.path.join(DIFFS_DIR, df)))
    return diffs

def reconstruct_version(diffs):
    """Reconstruct a version by applying diffs to base"""
    dmp = diff_match_patch()
    current_content = ""
    for patch_text in diffs:
        patches = dmp.patch_fromText(patch_text)
        current_content, _ = dmp.patch_apply(patches, current_content)
    return current_content

def save_diff(old_content, new_content):
    """Generate and save diff between old and new content"""
    dmp = diff_match_patch()
    patches = dmp.patch_make(old_content, new_content)
    patch_text = dmp.patch_toText(patches)
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    diff_path = os.path.join(DIFFS_DIR, f"{timestamp}.diff")
    write_file(diff_path, patch_text)
    return patch_text

def main():
    ensure_directory(DIFFS_DIR)

    # Get current document state
    current_content = get_current_content()
    if current_content is None:
        print(f"Error: {INPUT_FILE} not found!")
        return

    # Reconstruct expected state from base + diffs
    diffs = get_diffs()
    reconstructed_content = reconstruct_version(diffs)
    # Check if changes need to be tracked
    if reconstructed_content == current_content:
        print("No changes detected")
        return

    # Save new diff
    new_diff = save_diff(reconstructed_content, current_content)
    print(f"Saved new diff ({len(new_diff)} bytes)")
    
if __name__ == "__main__":
    main()