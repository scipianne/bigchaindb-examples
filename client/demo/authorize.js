'use strict';

import React from 'react';
import SimpleActions from '../lib/js/react/actions/simple_actions';

import BigchainDBConnection from '../../../lib/js/react/components/bigchaindb_connection';


(function authorize_class() {
    this.authorize = function() {
        SimpleActions.authorization({
            'user': document.getElementById("user").value,
            'password': document.getElementById("password").value
        });
    }

    this.meow = function() {
        alert('meow');
    }
});