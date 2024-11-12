FROM python:3.12.3

RUN apt-get update && \
	apt-get install -y python3 python3-pip git openssh-client

# Copy your SSH private key to the Docker container
COPY .ssh/id_ed25519 /root/.ssh/id_ed25519

# Set proper permissions for the SSH private key
RUN chmod 600 -R /root/.ssh/

# Add the Git repository host to known hosts
RUN ssh-keyscan github.com > /root/.ssh/known_hosts
# See: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints

COPY ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /backend
WORKDIR /backend

ENTRYPOINT ["/bin/bash", "/backend/entrypoint.sh"]