import os
import uuid

from azure.storage.blob import BlobServiceClient, ContainerClient
from flask import render_template, url_for

from app import app

# Creating the blob service client 
connect_str = "DefaultEndpointsProtocol=https;AccountName=storageacc7697;AccountKey=hg4Digr6VZgyo9+Q7jQRQ/g2TZX+nvemugwqVMTBSp7jSs/+mb6NnqVb5CgpL+kXg/6FeYGdVu96+AStAVgidQ==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Getting the existing container from the storage account
container_name = 'dummy-container'
container_client = blob_service_client.get_container_client(container_name)


@app.route("/")
@app.route("/index")
def index():
    blob_list = container_client.list_blobs()
    blob_names = [blob.name for blob in blob_list]
    return render_template('index.html', blobs=blob_names, container=container_name)
