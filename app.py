from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import boto3
from config import S3_HOST, S3_BUCKET, S3_REGION, S3_KEY, S3_SECRET

session = boto3.session.Session()

s3 = session.client(
    service_name='s3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET,
    endpoint_url=S3_HOST)

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

# Route to list the s3 files
@app.route('/files')
def files():
    # s3_resource = boto3.resource('s3')
    # my_bucket = s3_resource.Bucket(S3_BUCKET)
    # summaries = my_bucket.objects.all()

    # return render_template('files.html', my_bucket=my_bucket, files=summaries)
    return print(s3.list_buckets())
