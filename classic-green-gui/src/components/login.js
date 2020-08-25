import React, { Component } from 'react';
//import './App.css';
//import Modal from "./modal"

import FacebookLogin from 'react-facebook-login';

import GoogleLogin from 'react-google-login';

class LoginExpert extends Component {

  render() {

    const responseFacebook = (response) => {
      console.log(response);
    }

    const responseGoogle = (response) => {
      console.log(response);
    }

    return (
      <div className="App">
        <h1>LOGIN WITH FACEBOOK AND GOOGLE</h1>

      <FacebookLogin
        appId="235807680958859"
        fields="name,email,picture"
        callback={responseFacebook}
      />
      <br />
      <br />


      <GoogleLogin
        clientId="207424509626-itpddsft7ip76dra22tsr3v9cp47a21b.apps.googleusercontent.com" //CLIENTID NOT CREATED YET
        buttonText="LOGIN WITH GOOGLE"
        onSuccess={responseGoogle}
        onFailure={responseGoogle}
      />

      </div>
    );
  }
}

export default LoginExpert;