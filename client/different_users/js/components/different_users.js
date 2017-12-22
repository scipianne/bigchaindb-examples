import React from 'react';

import { Navbar } from 'react-bootstrap/lib';

import AccountList from '../../../lib/js/react/components/account_list';
import AccountDetail from './account_detail';
import LogInForm from './log_in_form';

import AssetActions from '../../../lib/js/react/actions/asset_actions';
import SimpleActions from '../../../lib/js/react/actions/simple_actions';

import BigchainDBConnection from '../../../lib/js/react/components/bigchaindb_connection';

//import request from '../../../lib/js/react/utils/request';

const Different_users = React.createClass({
    propTypes: {
        // Injected through BigchainDBConnection
        accountList: React.PropTypes.array,
        activeAccount: React.PropTypes.object,
        activeAsset: React.PropTypes.object,
        assetList: React.PropTypes.object,
        handleAccountChange: React.PropTypes.func,
        handleAssetChange: React.PropTypes.func,
        handleLogInClick: React.PropTypes.func,
        handleLogOutClick: React.PropTypes.func
    },

    fetchAssetList({ account }) {
        if (account) {
            AssetActions.fetchAssetList({
                account
            });
        }
    },

    authorization(json) {
        if (json) {
            SimpleActions.authorization(json);
        }
    },

    render() {
        const {
            accountList,
            activeAccount,
            activeAsset,
            assetList,
            handleAccountChange,
            handleAssetChange,
            handleLogInClick,
            handleLogOutClick
        } = this.props;

        return (
            <div>
                <Navbar fixedTop inverse>
                    <h1 style={{ textAlign: 'center', color: 'white' }}>Different users</h1>
                </Navbar>
                <div id="wrapper">
                    <div id="page-content-wrapper">
                        <div className="page-content">
                            <LogInForm
                                handleLogInClick={handleLogInClick}
                                handleLogOutClick={handleLogOutClick} />
                            <br/>
                            <AccountList
                                activeAccount={activeAccount}
                                appName="different_users"
                                className="row"
                                handleAccountClick={handleAccountChange}>
                                <AccountDetail
                                    accountList={accountList}
                                    activeAsset={activeAsset}
                                    assetList={assetList}
                                    handleAssetClick={handleAssetChange} />
                            </AccountList>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
});

export default BigchainDBConnection(Different_users);
