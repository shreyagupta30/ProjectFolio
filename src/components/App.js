import React from 'react';
import {Container} from 'react-bootstrap';
import Navbars from './Navbar';
import Homepage from './Homepage';

function App() {
  return (
    <>
      <Navbars />
      <Container>
        <Homepage />
      </Container>
    </>
  );
}

export default App;
