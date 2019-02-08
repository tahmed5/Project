FUNCTION VideoLoop():
    // Use OpenCV to attain video data
    cap = OpenCV.CaptureVideo()
    running = True

    while running:
        // Attain the individual frames
        image = cap.GetImage()
        // Display those frames to create a video loop
        OpenCV.showImage(image)

database config file:
dbconfig.txt
{
    // Data required to access the database
    user = 'username'
    password = 'password'
    host = 'raspberrypi.local'
    db = ['students', 'class']
    port = 'port'
}

FUNCTION dbConnect():
    // Open Config File
    config = open(dbconfig.txt,'r')
    // Connect To Database With Contents Of Config File
    db = Database.Connect(*config)]
    //Instantiate Cursor To Execute Commands
    cursor = db.cursor()

    return cursor
            

FUNCTION SaveImage(image):
    // If user is using a computer that they were logged into I can attain their username using the OS library
    username = os.getlogin()

    //Load Database Settings
    cursor = dbConnect()

    //Path To Where Image Will Be Saved 
    path = ./pi/images/username

    //Save Image To RaspberryPi
    OpenCV.save(path, image)

    //Save Path To Database
    cursor.execute('INSERT INTO Images (ImagePath) VALUES(path)')
    studentID = cursor.execute('SELECT StudentID FROM Students WHERE Username = username')
    imageID = cursor.execute('SELECT imageID FROM Images where ImagePath == path')
    cursor.execute('Insert INTO Student_Images (ImageID,StudentID) VALUES (studentID,imageID)')

class Facial_Recognition():
    FUNCTION Constructor():
        cascade = OpenCV.GetCascade('Haar Cascade') //Load Cascade
        recogniser = OpenCV.GetRecogniser('LBPH') // Load Recogniser
        recogniser.read('trainner.yml') // Load Classifer
        labels = open("labels.txt", 'r') // Load Labels

FUNCTION get_dims(image, res):
    DIMENSIONS = {
    "480p": (640,480),
    "720p": (1280,720),
    "1080p": (1920,1080),
    "4k": (3840,2160),
    }
    width,height = DIMENSIONS['480p']
    if res in DIMENSIONS:
        width,height = DIMENSIONS[res]

    change_res(cap, width, height)

FUNCTION change_res(cap,width,height):
    cap.height = height
    cap.width = width

FUNCTION setup():
    cascade = OpenCV.GetCascade('Haar Cascade') //Load Cascade
    recogniser = OpenCV.GetRecogniser('LBPH') // Load Recogniser
    image_dir = path.GetDir(images) //Get path to image directory
    cursor = dbConnect() //Connect to the database


    
