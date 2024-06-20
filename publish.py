import json
import time
from datetime import datetime
from google.cloud import pubsub_v1

# プロジェクトIDとトピックIDを設定
project_id = "project-name"
topic_id = "topic-name"

# PublisherClientを初期化
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def publish_message(message):
    """Pub/SubにメッセージをPublishする関数"""
    data = json.dumps(message).encode("utf-8")
    future = publisher.publish(topic_path, data)
    print(f"Published message ID: {future.result()}")

def main():
    """メイン関数：毎秒メッセージを生成してPublishする"""
    id = 10001
    name = "hoge"

    while True:
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = {
            "id": id,
            "name": name,
            "created_at": created_at
        }
        publish_message(message)

        # 1秒待機
        time.sleep(1)

if __name__ == "__main__":
    main()