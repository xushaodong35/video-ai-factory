from pipelines.video_to_scene import main as extract_scenes
from agents.vision_agent import analyze_scenes
from agents.product_swap_engine import ProductSwapEngine
from agents.blender_agent import generate_blender_script, save_script
import json


VIDEO_PATH = "input.mp4"
TARGET_PRODUCT = "YOUR_PRODUCT"


def run():
    print("\n🚀 ========== AI VIDEO FACTORY START ==========\n")

    # 1️⃣ 视频拆镜头
    print("🎬 Step 1: Extract scenes")
    scenes = extract_scenes(VIDEO_PATH)

    # 2️⃣ AI视觉理解
    print("🧠 Step 2: Vision analysis")
    vision = analyze_scenes(scenes)

    # 3️⃣ 产品替换
    print("🔄 Step 3: Product swap")
    engine = ProductSwapEngine()

    original = engine.detect_original_product(vision)

    swap_rules = engine.create_swap_rules(
        original_product=original,
        target_product=TARGET_PRODUCT
    )

    blender_config = engine.build_blender_config(swap_rules)

    # 保存替换逻辑
    with open("outputs/swap.json", "w", encoding="utf-8") as f:
        json.dump(blender_config, f, indent=2, ensure_ascii=False)

    # 4️⃣ Blender脚本生成
    print("🎥 Step 4: Generate Blender script")
    script = generate_blender_script(blender_config, vision)
    save_script(script)

    print("\n🎬 Step 5: READY TO RENDER IN BLENDER")

    print("\n✅ OUTPUT FILES:")
    print("- scenes.json")
    print("- vision.json")
    print("- swap.json")
    print("- render.py")

    print("\n🚀 ========== DONE ==========\n")


if __name__ == "__main__":
    run()
