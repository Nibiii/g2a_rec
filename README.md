## About The Project

The app is my recruitment assignment for junior DevOps position at G2A. It is supposed to provide simple API for managing and getting records from a relational database.
The app is based on flask and postgresql. If there is any need for the app to restart, the data shall persist because of an attached volume.


### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [PostgreSQL](https://www.postgresql.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.


### Prerequisites

* Docker
	```
	Go to https://docs.docker.com/get-docker/, choose suitable version and install it.
	```
* Docker-compose
	```
	Go to https://docs.docker.com/compose/install/, choose preferred scenario and follow the steps.
	```
	

### Installation

1. Open CMD/Terminal
2. Navigate to a target directory
3. Clone the repository
    ```sh
    git clone repo ./
    ```
4. Run docker-compose
	```sh
	docker-compose up
	```
5. The app is running! YEY!


### Usage
* App uses port 80 so remember to check if there is no app already listening on this port!
* To get existing parameter use *server_ip_address*/get?param=bar
* To set new/update existing parameter use *server_ip_address*/set?foo=bar
* To delete existing parameter use *server_ip_address*/delete?param=foo
