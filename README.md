# Azure Fundamentals
This is repository contains the flask app, that displays the names of all the files present in my Azure Container.
This is the first assignment of the MLOps-Azure training.
# Running the app on a local machine
In order to run the flask app, perform the following steps

1. Make sure you have set up the environment with all the dependencies.
2. Activate the virtual environment by typing `source azure_env/bin/activate`
2. Login to your Azure Account, using `az login` command in your terminal.
3. Go to the root directory of the project, that is just outside of the `app` folder in the project directory.
4. Run the command `flask run` and open `localhost:5000` in any browser.
5. Your app should run perfectly!

# Running the app deployed on the Azure Server
1. Make sure that the app is running on the Azure VM.
2. Click on the link [Azure App](azure-vm-dns.eastus.cloudapp.azure.com:5000).


# Project Directory
* `app`: This directory contains all the necessary html templates and `routes.py`.
* `templates`: This is a folder for all the html templates. There is one file `index.html`, which is displaying the filesnames of the files present in the blob. It also prints the name of the storage container.
* `routes.py`: It is responsible for defining the web routes of our web app. In this case, there is only one route, **index**. 

# Code Explanation
## `routes.py`
In this file, the code first connects with the Azure Storage Container and then fetches the blob names. 

* For creating a blob service client, the following code is executed
```
# Creating the blob service client 
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
```

* For connecting with a specific container, we provide the name of that container to the service client
```
# Getting the existing container from the storage account
container_name = '0c53dc52-f234-4404-b086-4dbb4e36042d'
container_client = blob_service_client.get_container_client(container_name)
```

* Using the container_client created above, the blob names are fetched and passed to `index.html` as a parameter.
```
def index():
    blob_list = container_client.list_blobs()
    blob_names = [blob.name for blob in blob_list]
    return render_template('index.html', blobs=blob_names, container=container_name)
```
# Billing Information
![](/billing_information.png)
