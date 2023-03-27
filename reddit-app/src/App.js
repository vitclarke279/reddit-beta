import React, { useState } from 'react';
import { Input, Button, List, ListItem, ListIcon } from '@chakra-ui/react';

const App = () => {
  const [subreddit, setSubreddit] = useState('');
  const [subreddits, setSubreddits] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch(`http://localhost:8000/reddit-api/stats/subreddit-mood?subreddit=${subreddit}`);
    const data = await response.json();
    console.log(data)
    const mood = data === 'positive' ? '😊' : '😔';
    setSubreddits([...subreddits, { title: subreddit, mood }]);
    setSubreddit('');
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <Input value={subreddit} onChange={(event) => setSubreddit(event.target.value)} />
        <Button type="submit">Add Subreddit</Button>
      </form>
      <List>
        {subreddits.map((subreddit) => (
          <ListItem key={subreddit.title}>
            <ListIcon as="span" fontSize="xl">
              {subreddit.mood}
            </ListIcon>
            {subreddit.title}
          </ListItem>
        ))}
      </List>
    </div>
  );
};

export default App;