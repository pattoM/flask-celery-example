# Flask-with-celery example
Sample code on using celery and celery beat with flask. 
Get an email containing a link to a coding question/topic on youtube every day. This is randomized with the youtube api 
but in future can be scaled and customized with machine learning etc. 

Check out devcoaster.com for more useful snippets/tutorials on specifics. 

### Running app locally or on heroku etc tips 
1. Flask app can be run as usual with `flask run` command. 
2. Run celery with `celery -A app.celery  worker --beat --loglevel=info` This command can be fed into a heroku worker and runs 
both celery beat and worker at once. It circumvents need for two workers which may be restricted on free plans on heroku. 
Don't scale this since consistency/duplicate problems may arise. 
3. Run `heroku ps:scale hybrid_worker=1` to scale worker to 1 dyno and start it. Do this after fresh deployments.
Restart dyno with `heroku restart hybrid_worker` and stop it with `heroku ps:stop hybrid_worker`
4. You need an api key to access the youtube api - get yours from google developer console after enabling youtube data api 

### Demonstated abilities 
1. Celery beat setup to run scheduled tasks executed by the celery worker in the background. 

### Live Demo 
Daily Coding Video 
https://daily-coding-video.herokuapp.com/ 

### Suggestions? 
Please open a pull request with your improvements so that this can be made better. 

### Future improvements
Check user locale, email using cron scheduling targeting certain times of day etc 