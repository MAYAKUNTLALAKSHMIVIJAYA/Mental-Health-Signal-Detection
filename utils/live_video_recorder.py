import cv2
import time
import tempfile

def record_live_video(duration=5):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Camera not accessible or already in use by another application.")

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_path = temp_video.name
    temp_video.close()

    out = cv2.VideoWriter(temp_path, fourcc, 20.0, (640, 480))
    start_time = time.time()

    print("Recording live video started...")

    try:
        while (time.time() - start_time) < duration:
            ret, frame = cap.read()
            if not ret:
                break

            out.write(frame)

            # Display recording preview window
            cv2.imshow("Recording 5s Clip... Press 'q' to stop early", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    print("Recording saved:", temp_path)
    return temp_path
