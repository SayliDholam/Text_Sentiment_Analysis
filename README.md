# Text_Sentiment_Analysis


<br/><br/>
to be updated
<br/><br/>
pip install textblob<br/>
pip install pandas<br/>
pip install streamlit<br/>
pip install clean-text[gpl]<br/>
pip install openpyxl <br/>
pip install matplotlib<br/>
pip install googletrans==4.0.0-rc1
</br>

Press Windows + R, type cmd, and hit Enter.<br/>
Navigate to the folder where your app.py is located using the cd command, then run the streamlit command -  <br/>
streamlit run filename.py
.


</br></br>

# Text_Sentiment_Analysis
The primary objective of this project is to allow the processing of data which 
comes from sources which are not in readily available state for analytical 
functions to work upon them.  
Here the concerned domain is the handwritten text base images from which text 
needs to be recognized, displayed and stored. </br>
This is where the application of OCR features, image processing, image storing, 
and alphabetical recognition become relevant.

</br>

## Technologies Used :
- **customertkinter : Python GUI library**<br/><br/>
 customtkinter is an extension of the standard Tkinter library for Python, designed to provide a more modern and customizable interface. It adds new features and widgets that are not available in the standard Tkinter library, making it easier to create visually appealing and responsive user interfaces.
<br/><br/> Features of customtkinter : <br/>
Modern Look: Offers a more modern and sleek look for the widgets compared to the traditional Tkinter.<br/>
Customization: Provides more options for customizing the appearance of widgets, including colors, shapes, and styles.
<br/><br/> You can install customtkinter using pip : <br/>
``` pip install customtkinter ```
<br/><br/>

- **PyTesseract : OCR**<br/>
PyTesseract is a Python wrapper for Google Tesseract-OCR, an optical character recognition (OCR) tool for extracting text from images. It allows you to use Tesseract's capabilities within Python programs
<br/><br/>Download and Install [PyTesseract](https://pypi.org/project/pytesseract/)
<br/><br/>Using pip command : <br/>
```pip install pytesseract pillow```<br/>
<br/>Write the below import in python code :<br/>
```from PIL import Image```<br/>
``` import pytesseract ```
<br/><br/>

- **MongoDB : Database**  <br/>
MongoDB is a popular NoSQL database that stores data in JSON-like documents with a flexible schema. This makes it different from traditional relational databases, which store data in rows and columns.</br></br>
Download MongoDB:</br>
Go to the [MongoDB Download Center](https://www.mongodb.com/try/download/community) and select the version that matches your operating system.</br></br>
Install MongoDB:</br>
Run the downloaded installer and follow the installation wizard.</br>
During installation, you can select the "Complete" setup type to install all MongoDB components.</br>
Ensure that the option to install MongoDB as a service is checked.</br></br>
Set up MongoDB Environment:</br>
After installation, you need to create directories for data and logs.</br>
``` md \data\db``` ```md \data\log ``` </br></br>
Run MongoDB:</br>
Open a command prompt and start the MongoDB server by running:</br>
``` "C:\Program Files\MongoDB\Server\{your_version}\bin\mongod.exe" ```</br></br>
Connecting to MongoDB:</br>
To interact with MongoDB, you can use the MongoDB shell or a GUI tool like MongoDB Compass.</br></br>
Using MongoDB with Python</br>
```pip install pymongo```</br></br>
Python Script:</br>
``` from pymongo import MongoClient ```
 
</br>

</br>
<br/>
<br/>

![system_design](system_diagram.jpg)
<br/>*System Diagram*

<br/>

![flowchart](flowchart.jpg)
<br/>*Flowchart*

<br/>

![er-diagram](er-diagram.jpg)
<br/>*Entity Relationship Diagram*

<br/>

![handwriting-recognition](handwriting-recognition.jpg)
<br/>*Handwriting Recognition*

<br/>

![database](database.jpg)
<br/>*Database*

<br/>
