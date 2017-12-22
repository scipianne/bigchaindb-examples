import SimpleActions from '../actions/simple_actions';

import request from '../../utils/request';


const SimpleSource = {
    postAuthorization: {
        remote(state) {
            const { err, payloadToPost, app } = state.meta;

            return request('authorize', {
                method: 'POST',
                jsonBody: payloadToPost
            });
        },

        success: SimpleActions.successAuthorization,
        error: SimpleActions.errorAuthorization
    }
};

export default SimpleSource;
