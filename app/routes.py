import os
import uuid

from azure.storage.blob import (BlobClient, BlobServiceClient, ContainerClient,
                                __version__)
from flask import render_template, url_for

from app import app

# Creating the blob service client 
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Getting the existing container from the storage account
container_name = '0c53dc52-f234-4404-b086-4dbb4e36042d'
container_client = blob_service_client.get_container_client(container_name)


@app.route("/")
@app.route("/index")
def index():
    blob_list = container_client.list_blobs()
    blob_names = [blob.name for blob in blob_list]
    return render_template('index.html', blobs=blob_names, container=container_name)
