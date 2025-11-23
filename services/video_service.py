import json
import os
from models.videoaula import VideoAula
from models.user import DATA_DIR


class VideoService:
    FILE_PATH = os.path.join(DATA_DIR, 'videoaulas.json')

    def __init__(self):
        self.videoaulas = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [VideoAula.from_dict(item) for item in data]

    def _save(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([v.to_dict() for v in self.videoaulas], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.videoaulas

    def get_by_id(self, vid):
        return next((v for v in self.videoaulas if v.id == vid), None)

    def add_video(self, video: VideoAula):
        self.videoaulas.append(video)
        self._save()
