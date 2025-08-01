🍎 Catch the Fruit Game with Mediapipe and OpenCV
This is a simple interactive computer vision game built using Python, OpenCV, and MediaPipe. The player raises their right hand to "catch" falling fruits on screen. The game uses real-time pose detection to track the player's wrist and detect collisions with falling fruit.

🎮 Game Description
A red fruit falls from the top of the screen.

The player must raise their right hand (wrist) to catch the fruit.

When the wrist intersects with the fruit, the score increases by 1.

Missed fruits are reset once they fall below the screen.

The game displays your score and FPS in real-time.

🧠 Features
Real-time pose detection using MediaPipe.

Wrist tracking and collision detection with a falling object.

Score tracking and visual feedback.

Lightweight, runs on a standard webcam feed.

📦 Requirements
Install the required Python packages using:

bash
Copy
Edit
pip install opencv-python mediapipe numpy
▶️ How to Run
Save the game code in a file, e.g., fruit_game.py.

Run the script:

bash
Copy
Edit
python fruit_game.py
Allow webcam access when prompted.

Raise your right hand to catch the fruit!

Press q to quit the game.

🧩 How It Works
MediaPipe Pose detects 33 body landmarks.

The game tracks the right wrist (landmark index 16).

A fruit falls with a set speed.

If the wrist is within a certain distance from the fruit, it's considered a catch.

The fruit resets and the score increases.



🛠️ Customization Ideas
Add different fruit types and assign varying points.

Introduce multiple falling fruits.

Track both hands for 2-player mode.

Add sound effects and animations.

Increase difficulty over time by speeding up fruit fall rate.

📄 License
This project is open-source and available under the MIT License.