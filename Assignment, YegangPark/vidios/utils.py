import isodate
from googleapiclient.discovery import build
import datetime

YT_API_KEY = "AIzaSyDzUnRWoaTp1WUF4Gh1tOyvCS71nmnM2u8"

def fetch_duration_with_api(url: str) -> datetime.timedelta | None:
    # 1) URL에서 videoId 추출
    import re
    m = re.search(r'(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})', url)
    if not m:
        return None
    video_id = m.group(1)

    # 2) API 클라이언트 구성
    youtube = build("youtube", "v3", developerKey=YT_API_KEY)
    resp = youtube.videos().list(
        part="contentDetails",
        id=video_id
    ).execute()

    items = resp.get("items", [])
    if not items:
        return None

    # 3) ISO 8601 기간 문자열 → timedelta
    duration_iso = items[0]["contentDetails"]["duration"]
    return isodate.parse_duration(duration_iso)