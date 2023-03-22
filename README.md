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

