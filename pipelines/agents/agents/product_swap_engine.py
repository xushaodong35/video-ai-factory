import json


class ProductSwapEngine:

    def detect_original_product(self, vision_data):
        """
        🔍 从视觉AI数据中识别原产品
        """

        for scene in vision_data.get("scenes", []):
            if "LED" in scene.get("product", ""):
                return "LED lamp"

        return "unknown_product"

    def create_swap_rules(self, original_product, target_product):
        """
        🔥 产品替换规则（核心商业逻辑）
        """

        return {
            "original": original_product,
            "target": target_product,

            # ✔ 保持不变
            "preserve": [
                "camera_motion",
                "lighting_setup",
                "scene_timing",
                "composition"
            ],

            # ❗ 替换部分
            "replace": [
                "3d_mesh",
                "material_shader",
                "surface_texture"
            ],

            # 🔥 光影匹配
            "lighting_match": {
                "mode": "preserve_original",
                "adapt_reflection": True
            }
        }

    def build_blender_config(self, rules):
        """
        🎬 转换为 Blender 可执行配置
        """

        return {
            "mode": "object_swap_only",
            "keep_scene": True,
            "apply_material_transfer": True,
            "lock_camera": True,
            "rules": rules
        }

    def export(self, config, output="product_swap.json"):
        with open(output, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

        print("✅ Product swap config saved:", output)


if __name__ == "__main__":

    engine = ProductSwapEngine()

    vision_data = {
        "scenes": [
            {
                "product": "LED lamp"
            }
        ]
    }

    original = engine.detect_original_product(vision_data)

    rules = engine.create_swap_rules(
        original_product=original,
        target_product="YOUR_PRODUCT"
    )

    config = engine.build_blender_config(rules)

    engine.export(config)
