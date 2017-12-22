import alt from '../alt';


class SimpleActions {
    constructor() {
        this.generateActions(
            'authorization',
            'successAuthorization',
            'errorAuthorization'
        );
    }
}

export default alt.createActions(SimpleActions);
