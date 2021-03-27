import React from 'react';
import ReactDOM from 'react-dom';
import App from "./App";
import Search from './components/Search'
import Table from './components/Table'
import { BrowserRouter as Router, Switch, Route} from "react-router-dom";

const Routing = () => {
    return(
      <Router>
        <Switch>
          <Route exact path="/" component={App} />
          <Route path="/Search" component={Search} />
          <Route path="/Table" component={Table} />
        </Switch>
      </Router>
    )
  }
  ReactDOM.render(
    <React.StrictMode>
      <Routing />
    </React.StrictMode>,
    document.getElementById('root')
  );
// ReactDOM.render( <App/>, document.getElementById('root') );
