import docker
from fastapi import FastAPI
import json

app = FastAPI()
client = docker.from_env()


# make index page
@app.get("/")
def index():
    return {"message": "Hello World"}
# Get a list of running containers

# Container operations


@app.get("/containers")
def get_containers():
    data_list = client.containers.list()
    response = []
    print(data_list)
    for data in data_list:
        print(data)
        response.append(data.name)
    return response


@app.get("/containers/{container_id}")
def get_container(container_id: str):
    return client.containers.get(container_id)


@app.post("/containers/{container_id}/start")
def start_container(container_id: str):
    container = client.containers.get(container_id)
    container.start()
    return {"message": "Container started"}


@app.post("/containers/{container_id}/stop")
def stop_container(container_id: str):
    container = client.containers.get(container_id)
    container.stop()
    return {"message": "Container stopped"}


@app.delete("/containers/{container_id}")
def delete_container(container_id: str):
    container = client.containers.get(container_id)
    container.remove()
    return {"message": "Container deleted"}

# Image operations


@app.get("/images")
def get_images():
    images = client.images.list()
    response = []
    for image in images:
        response.append(image.tags)
    return response


@app.get("/images/{image_id}")
def get_image(image_id: str):
    return client.images.get(image_id)


@app.post("/images/{image_id}/pull")
def pull_image(image_id: str):
    image = client.images.pull(image_id)
    return {"message": "Image pulled"}


@app.delete("/images/{image_id}")
def delete_image(image_id: str):
    client.images.remove(image_id)
    return {"message": "Image deleted"}

# Volume operations


@app.get("/volumes")
def get_volumes():
    data_list = client.volumes.list()
    response = []
    print(data_list)
    for data in data_list:
        print(data)
        response.append(data.name)
    return response


@app.get("/volumes/{volume_name}")
def get_volume(volume_name: str):
    return client.volumes.get(volume_name)


@app.post("/volumes/{volume_name}/create")
def create_volume(volume_name: str):
    client.volumes.create(volume_name)
    return {"message": "Volume created"}


@app.delete("/volumes/{volume_name}")
def delete_volume(volume_name: str):
    client.volumes.get(volume_name).remove()
    return {"message": "Volume deleted"}

# Network operations


@app.get("/networks")
def get_networks():
    data_list = client.networks.list()
    print(data_list)
    response = []
    for data in data_list:
        print(data)
        response.append(data.name)
    return response


@app.get("/networks/{network_id}")
def get_network(network_id: str):
    return client.networks.get(network_id)


@app.post("/networks/{network_id}/create")
def create_network(network_id: str):
    client.networks.create(network_id)
    return {"message": "Network created"}


@app.delete("/networks/{network_id}")
def delete_network(network_id: str):
    client.networks.get(network_id).remove()
    return {"message": "Network deleted"}

# System operations


@app.get("/system/info")
def get_system_info():
    return client.info()


@app.get("/system/version")
def get_system_version():
    return client.version()

# Config operations


@app.get("/configs")
def get_configs():
    data_list = client.configs.list()
    print(data_list)
    response = []
    for data in data_list:
        response.append(data.name)
    return response


@app.get("/configs/{config_id}")
def get_config(config_id: str):
    return client.configs.get(config_id)

# Secret operations


@app.get("/secrets")
def get_secrets():
    data_list = client.secrets.list()
    response = []
    for data in data_list:
        response.append(data.name)
    return response


@app.get("/secrets/{secret_id}")
def get_secret(secret_id: str):
    return client.secrets.get(secret_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3754)
