import json


def generate_blender_script(product_swap_data, vision_data):
    """
    🎬 将AI数据转换为Blender脚本
    """

    script = []

    script.append("import bpy\n")

    # 清空场景
    script.append("""
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
""")

    # 创建摄像机
    script.append("""
bpy.ops.object.camera_add(location=(0, -5, 2))
bpy.context.scene.camera = bpy.context.object
""")

    # 创建灯光
    script.append("""
bpy.ops.object.light_add(type='AREA', location=(2, 2, 5))
""")

    # 👉 产品替换核心逻辑
    rules = product_swap_data.get("rules", {})

    script.append(f"""
# ===== 产品替换逻辑 =====
# 原产品: {rules.get('original')}
# 新产品: {rules.get('target')}

# TODO: import your product model here
""")

    # 摄像机动画（模拟广告镜头）
    script.append("""
cam = bpy.context.scene.camera
cam.location = (0, -5, 2)
cam.keyframe_insert(data_path="location", frame=1)

cam.location = (0, -2, 2)
cam.keyframe_insert(data_path="location", frame=60)
""")

    script.append("\nprint('Render Ready')")

    return "\n".join(script)


def save_script(script, output="render.py"):
    with open(output, "w", encoding="utf-8") as f:
        f.write(script)

    print("✅ Blender script generated:", output)


if __name__ == "__main__":

    # 模拟输入
    product_swap_data = {
        "rules": {
            "original": "LED lamp",
            "target": "YOUR_PRODUCT"
        }
    }

    vision_data = {}

    script = generate_blender_script(product_swap_data, vision_data)
    save_script(script)
