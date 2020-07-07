# NLP API

Simple api to parse and apply some preprocessing steps in portuguses phrases (pt_BR)

This api uses the great FastAPI and spaCy packages!

## Usage

If you don't have docker and docker-compose please install both of them.

```bash
$> docker-compose up --build -d
```

Now you can access [http://localhost:8787](http://localhost:8787) to see a simple response.

Since this is build using FastAPI, you can interact with the api using their built in interface, just go to [http://localhost:8787/docs/](http://localhost:8787/docs/).

![Working example](output.gif)