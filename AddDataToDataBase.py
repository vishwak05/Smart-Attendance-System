import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://smartattendance-95405-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "21EG106B03":
    {
        "name":"Datha Prasad",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":5,
        "standing":"A",
        "year":4,
        "last_attendance_time":"2024-09-12 00:23:54"
    },
    "21EG106B04":
    {
        "name":"Shreya Gundoju",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":6,
        "standing":"B",
        "year":4,
        "last_attendance_time":"2024-09-18 00:23:54"
    },
    "21EG106B14":
    {
        "name":"Varsha",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":7,
        "standing":"O",
        "year":4,
        "last_attendance_time":"2024-09-17 00:23:54"
    },
    "21EG106B16":
    {
        "name":"Akshaya Jangiti",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":10,
        "standing":"A",
        "year":4,
        "last_attendance_time":"2024-09-16 00:23:54"
    },
    "21EG106B27":
    {
        "name":"Sahithi Pasham",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":11,
        "standing":"O",
        "year":4,
        "last_attendance_time":"2024-09-16 00:23:54"
    },
    "21EG106B28":
    {
        "name":"Prashanth Vallepu",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":6,
        "standing":"B",
        "year":4,
        "last_attendance_time":"2024-09-18 00:23:54"
    },
    "21EG106B29":
    {
        "name":"Vrudhi Shetty",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":14,
        "standing":"O",
        "year":4,
        "last_attendance_time":"2024-09-18 00:23:54"
    },
    "21EG106B30":
    {
        "name":"Manisha Ravulapally",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":16,
        "standing":"O",
        "year":4,
        "last_attendance_time":"2024-09-18 00:23:54"
    },
    "21EG106B38":
    {
        "name":"Vishwas",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":10,
        "standing":"A",
        "year":4,
        "last_attendance_time":"2024-09-18 00:23:54"
    },
    "21EG106B39":
    {
        "name":"Sai Kiran",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":8,
        "standing":"B",
        "year":4,
        "last_attendance_time":"2024-09-18 00:23:54"
    },
    "21EG106B46":
    {
        "name":"Venkat Sai Ram",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":10,
        "standing":"B",
        "year":4,
        "last_attendance_time":"2024-09-18 00:23:54"
    },
    "21EG106B47":
    {
        "name":"Aarusha Kondi",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":9,
        "standing":"A",
        "year":4,
        "last_attendance_time":"2024-09-12 0:12:45"
    },
    "21EG106B60":
    {
        "name":"Preetham",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":8,
        "standing":"O",
        "year":4,
        "last_attendance_time":"2024-09-17 00:23:54"
    },
    "22EG506B01":
    {
        "name":"Sai Kumar",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":10,
        "standing":"B",
        "year":4,
        "last_attendance_time":"2024-09-12 00:23:54"
    },
    "22EG506B04":
    {
        "name":"Akshitha Sedpur",
        "major":"Artificial Intelligence",
        "starting_year":2022,
        "total_attendance":6,
        "standing":"A",
        "year":4,
        "last_attendance_time":"2024-09-18 00:18:36"
    }
}

for key,value in data.items():
    ref.child(key).set(value)