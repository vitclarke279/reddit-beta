import React, { useState } from 'react';
import { Input, Button, List, ListItem, HStack, Container} from '@chakra-ui/react';
import { ImHappy2, ImSad2 } from 'react-icons/im';


const App = () => {
  const [subreddit, setSubreddit] = useState('');
  const [subreddits, setSubreddits] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch(`http://localhost:8000/reddit-api/stats/subreddit-mood?subreddit=${subreddit}`);
    const data = await response.json();
    const moodIcon = data === 'positive' ? <ImHappy2 /> : <ImSad2 />;
    setSubreddits([...subreddits, { title: subreddit, mood: moodIcon }]);
    setSubreddit('');
  };

  return (
    <div>
      <Container m={2}>
        <form onSubmit={handleSubmit}>
            <Input value={subreddit} onChange={(event) => setSubreddit(event.target.value)} />
            <Button type="submit">Add Subreddit</Button>
        </form>
        <List>
            {subreddits.map((subreddit) => (
            <HStack spacing={8}>
                {subreddit.mood}
                <ListItem key={subreddit.title}>
                {subreddit.title}
                </ListItem>
            </HStack>
            ))}
        </List>
        </Container>
    </div>
  );
};

export default App;