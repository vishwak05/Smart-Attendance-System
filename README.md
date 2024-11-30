# Smart Attendance System with Face Recognition

A real-time face recognition-based attendance system built with Python, OpenCV, and Firebase. The system automatically detects and marks attendance for registered students using facial recognition technology.

## Features

- Real-time face detection and recognition
- Automated attendance marking
- Firebase integration for data storage
- Student information display including:
  - Total attendance count
  - Academic details
  - Last attendance timestamp
- Duplicate entry prevention (30-second cooldown)
- Visual feedback modes for different states

## Prerequisites

- Python 3.7+
- OpenCV
- face_recognition
- firebase-admin
- cvzone
- numpy

## Installation

1. Clone the repository
   ```
   cd smart-attendance-system
   git clone https://github.com/yourusername/smart-attendance-system.git
   ```
2. Install required packages
   ```
pip install opencv-python face-recognition firebase-admin cvzone numpy
   ```

3. Set up Firebase:
   - Create a Firebase project
   - Download your `serviceAccountKey.json` from Firebase Console
   - Place it in the project root directory
   - Update the Firebase configuration in the code if necessary

## Project Structure

- `main.py` - Main application file for running the attendance system
- `EncodeGenerator.py` - Generates facial encodings for registered students
- `AddDataToDatabase.py` - Adds student information to Firebase
- `Resources/` - Contains background images and mode images
- `Images/` - Store student photos here
- `EncodeFile.p` - Generated encodings file

## Usage

1. Add student photos to the `Images/` directory (format: studentID.png)

2. Add student information to database:
```
python AddDataToDatabase.py
```
3. Generate encodings:
```
python EncodeGenerator.py
```
4. Run the main application:
```
python main.py
```

## How It Works

1. The system captures video feed from the camera
2. Detects faces in real-time
3. Compares detected faces with stored encodings
4. When a match is found:
   - Retrieves student information from Firebase
   - Displays student details
   - Updates attendance if eligible
   - Shows appropriate status messages

## Database Structure

### Students Collection
```
{
"studentID": {
"name": "Student Name",
"major": "Course Major",
"starting_year": "Year",
"total_attendance": "Count",
"standing": "Grade",
"year": "Current Year",
"last_attendance_time": "Timestamp"
}
}
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security Note

- Keep your `serviceAccountKey.json` secure and never commit it to version control
- Add it to your `.gitignore` file

