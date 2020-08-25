import React from "react";
import {Navbar, Nav,NavDropdown,FormControl,Form,Container} from 'react-bootstrap';
import { Button, } from 'react-bootstrap';
import '../App.css';
import '../bootstrap.css';
import classicGreenLogoIcon from '../img/logo-icon.png'
import classicGreenLogoText from '../img/logo_text.png'
import LoginExpert from './login.js'

import ModalComp from './createModal.js'




export class Navigation extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      modalState : false
    }
  }


  handleLoginClick = ()=>{
    console.log("------------------------login click kiya -------------------");
    this.setState({modalState:true})

  }
    render(){
      let modal = ""
      if(this.state.modalState){
        modal = <ModalComp modalContent = {<LoginExpert/>} isOpen={true}/>

      }
      let navContents = this.props.mainState.data2.map(categListItem=>{
        let categName = (categListItem.CatName+"s").toUpperCase()
        return (
          
<Nav.Link href="#home"><b>{categName}&nbsp;&nbsp;</b></Nav.Link>
        )

      })
        return(
          
<Navbar   className="vert-align" expand="lg" style={{}}>

  <Navbar.Brand href="#home" style={{display:'flex','flex-direction':'row'}}>
    <img style={{width:'70px',height:'55px'}} src={classicGreenLogoIcon} />
    {/* <h5 className = "style-company-name"> Classic Green</h5> */}
    <img style={{width:'200px',height:'55px', 'marginLeft':'-10%',"marginTop":"3%",}} src={classicGreenLogoText} />&nbsp;&nbsp;&nbsp;
  </Navbar.Brand>
  <Navbar.Toggle aria-controls="basic-navbar-nav" />
  <Navbar.Collapse id="basic-navbar-nav" >
  
    {/* <Nav className="mr-auto"> */}
    <Nav className="navbar-contents">
    <Nav.Link href="/" target="_blank"><b>HOME&nbsp;&nbsp;</b></Nav.Link>
      {navContents}
      <Nav.Link onClick={this.handleLoginClick}><b>Login&nbsp;&nbsp;</b></Nav.Link>  
      <Nav.Link href="http://localhost:8000/garpan" target="_blank"><b>Register&nbsp;&nbsp;</b></Nav.Link>
      {modal}
    </Nav>
    
   </Navbar.Collapse>
</Navbar>

          )
      }
  }



