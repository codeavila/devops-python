import pulumi
from pulumi import Config
import pulumi_docker as docker

config = Config()
host_port = config.get_int("hostPort") or 5000

image = docker.Image(
    "hello-image",
    build=docker.DockerBuild(context="./hello_app"),
    image_name="pulumi-docker-hello:latest",
)

container = docker.Container(
    "hello-container",
    name="pulumi-docker-hello",
    image=image.image_name,
    ports=[docker.ContainerPortArgs(internal=5000, external=host_port)],
)

pulumi.export("imageName", image.image_name)
pulumi.export("containerName", container.name)
pulumi.export("url", f"http://localhost:{host_port}")
