import cv2
import json


def extract_scenes(video_path):
    """
    🔥 简化版视频拆镜头（Phase 2基础版）
    """

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    duration = frame_count / fps if fps > 0 else 0

    scenes = []

    # 👉 先做“粗粒度分镜”（每2秒一个镜头）
    step = 2.0
    t = 0
    scene_id = 0

    while t < duration:
        scenes.append({
            "id": scene_id,
            "start": round(t, 2),
            "end": round(min(t + step, duration), 2),
            "description": "auto-detected scene (placeholder)",
            "product": "unknown"
        })

        t += step
        scene_id += 1

    cap.release()

    return scenes


def save_scenes(scenes, output="scenes.json"):
    with open(output, "w", encoding="utf-8") as f:
        json.dump(scenes, f, indent=2, ensure_ascii=False)

    print("✅ scenes saved:", output)


def main(video_path="input.mp4"):
    scenes = extract_scenes(video_path)
    save_scenes(scenes)
    return scenes


if __name__ == "__main__":
    main()
