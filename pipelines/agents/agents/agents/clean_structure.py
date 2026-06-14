import os
import shutil

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_file(src, dst_dir):
    if os.path.exists(src):
        ensure_dir(dst_dir)
        shutil.move(src, os.path.join(dst_dir, os.path.basename(src)))
        print(f"Moved {src} → {dst_dir}")

def main():

    print("🧹 Cleaning project structure...")

    # 创建标准目录
    ensure_dir("agents")
    ensure_dir("pipelines")
    ensure_dir("outputs")

    # 移动文件（如果你现在都在根目录）
    move_file("vision_agent.py", "agents")
    move_file("product_swap_engine.py", "agents")
    move_file("blender_agent.py", "agents")
    move_file("video_to_scene.py", "pipelines")

    print("✅ Structure cleaned!")

    print("""
Final structure should be:
- run.py
- agents/
- pipelines/
- outputs/
""")

if __name__ == "__main__":
    main()
