# GAE Blog
A Google App Engine-based blog application 

 - Built with **Python 3.9+ and Flask** 
 - Data is stored in **Google Cloud Datastore** (a.k.a Firestore in Datastore Mode) 
 - You can customize the theme (e.g. change the colors)

<img src="https://storage.googleapis.com/nocommandline-blog.appspot.com/gae_blog_app/home_page.png?latest=true" alt="Sample Blog Home Page Screenshot" title="Sample Blog Home Page Screenshot" style="margin: 0 auto; max-width: 600px">

## Setup 
1. Clone the repo or download the source as a zipped file and unzip it to a folder
2. If you're using the GAE GUI - [NoCommandLine](https://nocommandline.com/), then follow the steps to add an existing project i.e. 

    a. File > Add Existing Application 
    
    b. In the Application Path, use the file widget to navigate to the folder from bullet 'a' and select the `app.yaml` file 
    
    c. Provide a new name for your App 
    
    d. Click the 'Add' button 

    e. Open `main.py` and update the port number to the value auto generated by `NoCommandLine` (the value in the 'Port' Column) 
    
    f. Finally, click the 'Run' icon. This will install the requirements from the `requirements.txt` file and start the App.
    
3. If you're not using the GAE GUI - [NoCommandLine](https://nocommandline.com/)

    a. Open a terminal window 
    
    b. Change directory to the folder where you unzipped the project i.e. `$cd <project_path>` 
    
    c. Create and activate a virtual env
    
    - `python3 -m venv env` 
    - `source env/bin/activate`
    
    d. Install the requirements 
    
    - `pip3 install -r requirements.txt`
    
    e. Run the app using the command - `python main.py`
 

## Not Covered
1. Comments Module
2. Subscribe to Blog Module

## Screenshots

1. ### Admin Page 
<img src="https://storage.googleapis.com/nocommandline-blog.appspot.com/gae_blog_app/admin_page.png" alt="Admin Page Screenshot" title="Admin Page Screenshot" style="margin: 0 auto; max-width: 600px; margin-bottom:20px;"> 

2. ### New Post 
<img src="https://storage.googleapis.com/nocommandline-blog.appspot.com/gae_blog_app/new_post_page.png" alt="New Post Page Screenshot" title="New Post Page Screenshot" style="margin: 0 auto; max-width: 600px; margin-bottom:20px;"> 

3. ### Sample Post  
<img src="https://storage.googleapis.com/nocommandline-blog.appspot.com/gae_blog_app/sample_post.png" alt="Sample Post Screenshot" title="Sample Post Screenshot" style="margin: 0 auto; max-width: 600px; margin-bottom:20px;">
