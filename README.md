## Gesture-Controlled Media Player for Visual Accessibility

This project uses computer vision and hand tracking to create a media player that can be controlled entirely with hand gestures. It's designed with visual accessibility in mind, aiming to make it easier for visually impaired individuals to enjoy music and videos without relying solely on traditional interfaces.

## Why This Matters

* **Accessibility:** Visually impaired people often face challenges using standard media players that rely heavily on visual cues. This project empowers them to control playback, adjust volume, and navigate through media using intuitive hand gestures.
* **Independence:** The gesture-based interface promotes greater independence, allowing users to enjoy media without requiring assistance from others.
* **Inclusivity:** This project demonstrates the potential of technology to create inclusive solutions that cater to a wider range of users.


## How It Works

1. **Hand Tracking:** The program uses OpenCV's `HandDetector` module from the `cvzone` library to detect and track the user's hand in real-time video from the webcam.

2. **Gesture Recognition:** It identifies specific hand poses or gestures, such as:
   * One finger raised: Play/Pause
   * Two fingers raised: Volume Up
   * Middle finger raised: Volume Down
   * Four fingers raised (right hand): Next track
   * Four fingers raised (left hand): Previous track

3. **Action Execution:**  Once a gesture is recognized, the program uses `pyautogui` to simulate keyboard shortcuts that control VLC Media Player, performing the corresponding action.

4. **VLC Activation (Optional):** If VLC is not already the active window, the script uses `psutil` to find the VLC process and bring it to the foreground.


## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   (Make sure `requirements.txt` includes `opencv-python`, `cvzone`, `pyautogui`, and `psutil`)

## Usage

1. **Start VLC Media Player:** Ensure VLC is open and playing your media.
2. **Run the Script:**
   ```bash
   python3 main2.py 
   ```
3. **Control with Gestures:** Position your hand in front of the webcam and use the gestures described above to control VLC.

## Customization

* **Gesture Actions:** You can easily modify the `gesture_actions` dictionary to map different gestures to various VLC hotkeys or even control other media players.
* **Sensitivity:**  The `detectionCon` parameter in the `HandDetector` initialization can be adjusted to fine-tune hand detection sensitivity.

## Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or suggest new features.

## License

This project is licensed under the [MIT License](LICENSE).
