from flask import Flask, render_template,jsonify

app = Flask(__name__)

Project = [
  {
    'id': 1,
    'title': 'Django Project',
    'platform':'vs code',
    'description':'This is a project for learning django'  
  },
  {
    'id': 2,
    'title': 'Flask Project',
    'platform':'pycham',
    'description':'This is a project for learning Flask'  
  },
  {
    'id': 3,
    'title': 'Login pages',
    'platform':'vs code',
    'description':'This is login page for upload on your website'  
  },
  {
    'id': 4,
    'title': 'Templates',
    'description':'This is a project for use templates'  
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html',projects=Project)

@app.route('/api/project')
def project():
  return jsonify(Project)



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
