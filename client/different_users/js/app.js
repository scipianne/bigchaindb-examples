// Install necessary polyfills (see supported browsers) into global
import 'core-js/es6';
import 'core-js/stage/4';
import 'isomorphic-fetch';

import React from 'react';
import ReactDOM from 'react-dom';

import Different_users from './components/different_users';

import '../../lib/css/scss/main.scss';


const App = () => (
    <div className="app different_users">
        <Different_users />
    </div>
);

ReactDOM.render(<App />, document.getElementById('bigchaindb-example-app'));
