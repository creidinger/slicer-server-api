from flask import Flask
from flask_s3 import FlaskS3

app = Flask(__name__)
app.config['FLASKS3_BUCKET_DOMAIN'] = 'http://192.168.1.226:9000'
app.config['FLASKS3_BUCKET_NAME'] = 'perceptengine'
app.config['FLASKS3_REGION'] = 'us-east-1'
app.config['FLASKS3_URL_STYLE'] = 'path'
app.config['AWS_ACCESS_KEY_ID'] = 'VSZACDCGYKSFWAGJGCXF'
app.config['AWS_SECRET_ACCESS_KEY'] = 'xUUDtJbSjB9XxUjwjRwj7m5CLe2EzaNbbCpnXsAM'


s3 = FlaskS3(app)

s3 = FlaskS3()
