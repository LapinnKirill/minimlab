import docker

def _id(client: docker.DockerClient, name: str) -> str | None:
    try:
        container = client.containers.get(name)
        return container.short_id
    except docker.errors.NotFound:
        return None
