# Inventory-Management

## This Project was built as a part of a job application at shopify. It has not been maintained for a very long time, so please contact me if you run into error when running this project.

To run this Django project in you local machine. Follow the steps described below.

1) Download the repository
2) Download and Install python [ version >= Python 3.10.0] -> Check if you have python already installed before reinstalling: Use: python --version in your terminal/cmd.
3) Make sure you have running internet connection as this project uses Bootstrap CDN for the frontend design.
4) There is a file called requirements.txt 
5) In your cmd/terminal run: python -m pip install -r requirements.txt [ make sure you are in the same directory as the requirements.txt file otherwise you will have to mention the full path of the file] 
7) open a command prompt or terminal and cd into the directory of this project 


9) to cross check you are in the right directory: run dir / ls according to your os. The command should return a list of these files and directories shown below:


![again_github](https://user-images.githubusercontent.com/65969795/148880978-3018568b-ae36-432c-8bb1-c449add8d07c.png)



10) run: python manage.py makemigrations 
11) now run: python manage.py migrate
12) run: python manage.py runserver
13) Now the web server should start and you should be able to access it from your browser. 

![Django-shopify_github](https://user-images.githubusercontent.com/65969795/148880032-ebc00208-be26-4b06-bfc1-b9394f90e7a2.png)

You will be able to see a link like one highlighted above in your terminal/command prompt. Use that link to access this server in your browser.

[SPECIAL NOTE]
As asked, all the CRUD functionalities are implemented in this project. Plus the additional functionality added is the ability to export Product Data to a csv file by pushing a button is added. It can be clearly seen on the navbar menu. No data exists in the database, but you can add it by yourself. Various options are accessible from the navbar menu. Also, the Tag field used in this project is for the purpose of categorizing various prodcts in the inventory. One product can have multiple tags.


Thank you for your time and for following these steps clearly. If any problem occurs, contact me at: adhikaririshik@gmail.com
