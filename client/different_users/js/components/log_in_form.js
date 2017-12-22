import React from 'react';

import classnames from 'classnames';
import { Col } from 'react-bootstrap/lib';
import { safeInvoke } from 'js-utility-belt/es6';

import Assets from './assets';


const LogInForm = React.createClass({
    propTypes: {
        handleLogInClick: React.PropTypes.func,
        handleLogOutClick: React.PropTypes.func
    },

    getInitialState() {
        return {
            user: "",
            password: "",
            username: "Guest"
        };
    },

    updateUser(user) {
        this.setState({
            user: user.target.value
        });
    },

    updatePassword(password) {
        this.setState({
            password: password.target.value
        });
    },

    handleLogInClick() {
        const { handleLogInClick } = this.props;

        safeInvoke(handleLogInClick, this.state.user, this.state.password);

        this.setState({
            username: "User " + this.state.user
        })
        this.setState({
            user: "",
            password: ""
        });
    },

    handleLogOutClick() {
        const { handleLogOutClick } = this.props;

        safeInvoke(handleLogOutClick);

        this.setState({
            user: "",
            password: "",
            username: "Guest"
        });
    },

    render() {
        return (
            <Col sm={6} md={6} lg={4} xl={3}>
                <div className="card">
                    <h4 style={{ textAlign: 'center' }}>Logged in as {this.state.username} </h4>
                    <br/>
                    User: <input type="text" value={this.state.user} onChange={this.updateUser} />
                    <br/>
                    Password: <input type="password" value={this.state.password} onChange={this.updatePassword} />
                    <br/>
                    <button onClick={this.handleLogInClick}>Log In</button>
                    <br/>
                    <button onClick={this.handleLogOutClick}>Log Out</button>
                    <br/>
                </div>
            </Col>
        );
    }
});

export default LogInForm;
