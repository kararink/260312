"""
Ritsuto Style Injector

Outputs the pure "style context" for Ritsuto's writing.
This does NOT include format/structure templates - those are handled by workflows.

Usage:
    python style_injector.py --topic "Your Topic"
"""

import argparse
import os
import glob

# Constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
STYLE_EXAMPLES_DIR = os.path.join(RESOURCES_DIR, "style_examples")

# User Profile Path (Set via environment variable or default to ~/product path)
USER_PROFILE_DIR = os.environ.get(
    "RITSUTO_PROFILE_DIR",
    os.path.join(os.path.expanduser("~"), "product", "Ritsuto_Brain", "00_システム", "00_UserProfile")
)


def read_file(path):
    """Reads a file and returns its content."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[File not found: {os.path.basename(path)}]"
    except Exception as e:
        return f"[Error reading {os.path.basename(path)}: {e}]"


def load_user_profile():
    """Loads core style files from the user profile."""
    profile_content = "# User Profile Context\n\n"
    
    files_to_load = [
        "00_マスター(Master_Context).md",
        "01_価値観(Core_Values).md",
        "03_執筆スタイル(Style_Guidelines).md"
    ]
    
    for filename in files_to_load:
        path = os.path.join(USER_PROFILE_DIR, filename)
        content = read_file(path)
        profile_content += f"## From {filename}\n{content}\n\n"
        
    return profile_content


def load_style_examples():
    """Loads all style examples from the style_examples directory."""
    examples_content = "# Style Examples (Few-Shots for Style Mimicry)\n\n"
    examples_content += "Use these examples to understand Ritsuto's writing STYLE (tone, rhythm, word choice).\n"
    examples_content += "Do NOT copy the structure - structure is determined by the workflow.\n\n"
    
    if not os.path.exists(STYLE_EXAMPLES_DIR):
        examples_content += "[No style examples directory found]\n"
        return examples_content
    
    md_files = glob.glob(os.path.join(STYLE_EXAMPLES_DIR, "*.md"))
    
    if not md_files:
        examples_content += "[No style examples found]\n"
        return examples_content
    
    for filepath in md_files:
        filename = os.path.basename(filepath)
        content = read_file(filepath)
        examples_content += f"## {filename}\n{content}\n\n---\n\n"
    
    return examples_content


def main():
    parser = argparse.ArgumentParser(
        description="Ritsuto Style Injector - Outputs style context for writing"
    )
    parser.add_argument(
        "--topic", 
        required=True, 
        help="The topic to write about"
    )
    
    args = parser.parse_args()
    
    # 1. Load User Profile (Style Rules)
    user_profile = load_user_profile()
    
    # 2. Load Style Examples (Few-Shots)
    style_examples = load_style_examples()
    
    # 3. Assemble Final Output
    final_output = f"""
{user_profile}

{style_examples}

---

# Writing Task

**Topic**: {args.topic}

**Instructions**:
1. Write in Ritsuto's style as defined above.
2. Apply the "Vertical Rhythm" formatting strictly.
3. Use the vocabulary and tone patterns from the style guide.
4. The STRUCTURE/FORMAT will be provided separately by the workflow - focus only on STYLE.
"""
    
    print(final_output)


if __name__ == "__main__":
    main()
