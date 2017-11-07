import os
import bottle support*

@route('/')
def index():
  return "Halló Heroku"
  

run(host='0.0.0.0',port=os.environ.get('PORT'))
