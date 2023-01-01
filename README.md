# PyPixoo

Python project for the Pixoo64

Documentation: [GitHub Pages](https://numbertheory.github.io/PyPixoo/)


## Install 

After cloning down the repo, and activating a virtual environment, run this:

```bash
pip install .
```

## Documentation

The documentation uses Jekyll and an older version of Ruby, so it's best to use the Docker commands below to build the documentation locally. You can also run it locally, if you have the correct version of Ruby, but I was unable to get it to work on a Apple Silicon (Mac M1).

When running the documentation locally, you'll be able to see your local changes at http://0.0.0.0:4000.

### Build the container
```bash
docker build -t docs:local docs/
```

### Run the documentation container

```bash
docker run -d -v $PWD/docs:/docs -p 4000:4000 docs:local
```

As you change the content of the docs, the container will detect those changes and rebuild the docs. To see it in the browser, refresh the browser at http://0.0.0.0:4000.

### Stop the container

```bash
docker stop $(docker ps --filter ancestor=docs:local --format '{{.Names}}')
```

