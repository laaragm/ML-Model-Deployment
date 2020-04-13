Machine Learning Model Deployment with Flask and Docker

The machine learning model itself is not the main object of study here, but it's available at https://github.com/laaragm/Data-Science-Enem2016/blob/master/Regression%20(Enem%20Random%20Forest%20Regressor).ipynb and you might check it out if you want.

In case you don't have docker installed, open the terminal and run:	
$ sudo apt install docker
$ sudo apt install docker-compose

In case you don't have pip installed, open the terminal and run:
$ sudo apt-get -y install python3-pip

Make sure everything is working fine by running each code separately. 
First of all, run the code you're using to train the model (the one which also has the predict function).
Run application.py (our API Rest) using the following commands:
$ FLASK_APP=application.py
$ FLASK_ENV=development
$ flask run

Now, if everything's working you can run(also, don't forget to do this in your project's folder):
$ docker-compose up

If you get a "permission denied" message: https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket

If everything works fine you'll a message like this(after running docker-compose up): 
"Starting ..........
Attaching to .......
.
.
.
Running on ....... 
Debbuger is active!
Debugger PIN: ........ "


Open another terminal and run (make sure to do it in your project's folder):
$ curl -d @data_to_predict.json http://0.0.0.0:5000/predict


