# Background
- Take some Reddit data and create a simple API endpoint to serve up that data (using Python/Rest).
- Use created API endpoint to build up a "Reddit homepage" using JavaScript. Could include a new way to list posts, an image gallery or anything else.
- Some Reddit data can be downloaded here: https://files.pushshift.io/reddit/

## Thoughts
- Need to interpret the reddit data available.
- Pushshift API available to extract data: https://github.com/pushshift/api
- What should be shown on the home page?
    - A line graph showing the activity level every hour (measured in the amount of comments made) of the top 10 active subreddit threads in the last 24 hours.
    - Can have a pill component above the graph to add filters if wanted to refine by key words and location. Location can default to the user's locale.
    - To the right of the graph have the hyperlinks to the top ten subreddits, also color codded to double up as a legend.

## Approach
- FastApi service which will interact with the Pushshift API to retrieve data.
- React client side to interact with the FastApi app.
- Use Docker to run the services locally.

## Development

### Dependencies
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Install [make](https://www.gnu.org/software/make/). For Linux, use your distribution's package manager e.g. Ubuntu: `sudo apt-get install make`

### Running
- run: `make start`

### API documentation
There are two ways to access the API documentation. With the app running:

- go to: [localhost:8000/docs](http://localhost:8000/docs)
- Or go to: [localhost:8000/redoc](http://localhost:8000/redoc)

### Accessing Reddit Home page
- go to: [localhost:3000](http://localhost:3000)


### Running backend tests
You can run the backend tests from inside your container:
 1. `make start` - ensure your containers are running first
 1. `make shell` - in a separate window
 2. `pytest <PATH_TO_YOUR_TEST>` - if you don't supply a path to a test, the whole test suite will run

