# Face-Recognition-Server

A Flask API server to store faces in a MongoDB collection and check new images for familiar faces and return their names, processed image, and audio of names to aid visually impaired people. 
This implementation is deployed on Heroku with MongoDB Atlas, you can change the link for your own Mongo Client.

req.py is a script to test the server and save the image and audio results, you can also change the link for your server app.

Images and audio are sent as base64 encoded data for better transmission, especially if the server is used with a mobile app.

The API takes input as json with the following form:

  {
  
    "img": *A base64 encoded image*,
    
    "name": *The name you want to save*,
    
    "save": *bool*
    
  }
  
If save = 1, it saves the face in the image with the sent name, else if save = 0, it checks the faces in the image for matches in the saved faces in the database and ignores the sent name.

For save = 0, the response code is 204 no content, for save = 1 the response is also json with the following form:

  {
  
    "img": *The sent image with bounding boxes around recognized faces, base64 encoded*,
    
    "names": *A list of strings, the recognized names*,
    
    "sound": *Sound bytes of text-to-speech applied on the names, base64 encoded*
    
   }
   
