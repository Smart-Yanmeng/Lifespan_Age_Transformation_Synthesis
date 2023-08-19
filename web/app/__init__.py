from flask import Flask

app = Flask(__name__)
app.template_folder = 'C:/Users/yorky/Desktop/STUDY/Python/interesting_project/Lifespan_Age_Transformation_Synthesis/web/app/templates'

from web.app import routes
