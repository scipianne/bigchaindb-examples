import alt from '../alt';

import SimpleActions from '../actions/simple_actions';
import SimpleSource from '../sources/simple_source';


class SimpleStore {
    constructor() {
        this.meta = {
            err: null,
            payloadToPost: null,
            app: null
        };
        this.bindActions(SimpleActions);
        this.registerAsync(SimpleSource);
    }

    onAuthorization(json) {
        this.meta.payloadToPost = json;
        this.getInstance().postAuthorization();
    }

    onSuccessAuthorization(result) {
        if (result == 'success!') {
            this.meta.payloadToPost = null;
        } else {
            this.meta.err = new Error('Authorization error');
        }
    }

    onErrorAuthorization(err) {
        this.meta.err = err;
    }
}

export default alt.createStore(SimpleStore, 'SimpleStore');
