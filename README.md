# Stock Analyser

Project implements a stock-analyser API.

The project is implemented using Flask Framework with Python 3.9. We also use Docker to make it easier to deploy and also for tests on local environment.

## Installation

In order to use the project `docker-compose` is probably going to be enough to execute the project. It might be necessary to install the projects dependencies before execute it, what can be done with following command:

```bash
pip install -r requirements.txt
```

## Usage

After install the dependencies, you can use following commands to execute the Docker instance at your local environment:
1. Build dockerfile : `docker-compose build`
2. Make system up: `docker-compose up`
3. Make system down: `docker-compose down`

To run the created tests it will be necessary to follow these steps:
1. Run tests: `pytest`

To run the documentation:
1. Run: `mkdocs serve`
2. Open the browser on the informed url

## Postman Requests
A sample of the possible requests for the system are presented at `stock-analyser.postman_collection.json` file and can be imported at Postman for local usage.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
