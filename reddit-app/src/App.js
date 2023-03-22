import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/')
      .then(response => setMessage(response.data.Hello))
      .catch(error => console.log(error));
  }, []);

  return (
    <div className="RedditApp">
      <header className="App-header">
        <p>
          {message}
        </p>
      </header>
    </div>
  );
}

export default App;
