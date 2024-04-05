## How To Analyse Stock Information?

If you want to retrieve historical data and analyse it, so
you're in luck! The `stock-analyser` package can help you
get this done.

Download the code from this GitHub repository and run some
Docker commands to get a running API to do it for you:

```shell
docker-compose build
docker-compose up
```

### Endpoints

#### Ping

- **Method**: GET
- **URL**: `http://127.0.0.1:5000/ping`

#### Tickers

- **Method**: GET
- **URL**: `http://127.0.0.1:5000/tickers`

#### Post

- **Method**: POST
- **URL**: `http://127.0.0.1:5000/tickers`
- **Body**:
  ```json
  {
      "tickers": ["AAPL"]
  }
