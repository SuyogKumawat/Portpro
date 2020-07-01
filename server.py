from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)              #here Flask is class and app is instance
print(__name__)                       #name of our app is main

@app.route('/')                    #here its decorator
def landing_page():
	return render_template('index.html')

# @app.route('/work.html')                    #here its decorator
# def work():
# 	return render_template('work.html')

# @app.route('/about.html')                    #here its decorator
# def about():
# 	return render_template('about.html')

# @app.route('/contact.html')                    #here its decorator
# def contact():
# 	return render_template('contact.html')


# @app.route('/works.html')                    #here its decorator
# def works():
# 	return render_template('works.html')

# @app.route('/index.html')                    #here its decorator
# def index():
# 	return render_template('index.html')

#we just copy and paste but now we have to make this site dynamic let see how we do that:-
@app.route('/<string:page_name>')                    #here its decorator
def index(page_name=None):
	return render_template(page_name)
#we will learn contact form it is not real unless people will contatc u and send a message 
# We will see further send info to our server in the backend and actually capture it and save it ans store it somewhere
# """So we will create actual contact page where users can submit contact info and 
# enter a message so that they can talk to u

# request object is used to grab information from the browser using request object

@app.route('/submit_form', methods=['POST', 'GET'])      
# #get means browser wants us to send info and post means browser want us to save info
def submit_form():
	# return 'form submitted hooraay!'
    if request.method == 'POST':
    	data=request.form.to_dict()          #all data in dictionary
    	write_to_csv(data)                  #we just print that data to our console in form of dictionary
    	return redirect('/thanku.html')
    else:
    	return 'Something went wrong try again'
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('login.html', error=error)

    #icon is added to the site by move our downloaded icon to assets folder
    #now we give thank you message by copying contact.html and delete the form tag 
    # and type thank you message in copied file there then in server.py file using
     # redirect redirect that contact.html to thanku.html(copied of contatc.html)

# up till now we have output on console but after closing console
 # output delets so we have to store it somewhere
 #We will now see how to store data 

 # ""as soon as server stops running or crashes,that data is lost bcoz that info of form is in memory,
 # ideally we write somewhere on disk so that even if we stop the server
 # that info still somewhere on file this file lives on this computer 
 # so how can we do this????""

# def write_to_file(data):
# 	with open ('database.txt',mode='a') as database:
# 		email=data["email"]
# 		subject=data["subject"]
# 		message=data["message"]

# 		my_file=database.write(f'\n{email},{subject},{message}')
 #better way to store in database is we can store it either in csv file or in excel file
 # The so-called CSV (Comma Separated Values)
 # format is the most common import and export format for spreadsheets and databases.

def write_to_csv(data):
	with open ('database1.csv',mode='a',newline='') as db:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]

		csv_write=csv.writer(db,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_write.writerow([email,subject,message])