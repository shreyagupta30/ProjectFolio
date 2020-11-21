import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Navbar from './Navbar';
import Homepage from './Homepage/Homepage';
import OrgList from './ProjectsList/OrgPage';
import OrgIndPage from './OrgIndPage/OrgIndPage'
import Footer from './Footer';

function App() {
  return (
    <>
    <Router>
      <Navbar />
      <Switch>
        <Route exact path="/" component={Homepage} />
        <Route exact path= "/projects" component={OrgList} />
        <Route exact path="/org" component={OrgIndPage} />
      </Switch>
      <Footer />
    </Router>
    </>
  );
}

export default App;
