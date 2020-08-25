
import Modal from 'react-bootstrap/Modal' 

import React from "react";
import { Button, } from 'react-bootstrap';
import '../App.css';

class ModalComp extends React.Component{
  constructor(props){
    super(props)
    this.state = {
      isOpen :this.props.isOpen
    }
  }
  componentWillReceiveProps(nextProps){
    this.setState({
      isOpen: nextProps.isOpen

    });
  }
    handleClose = () => {
      this.setState({isOpen:false})
    };
  render(){
    return (
 
        <Modal show={this.state.isOpen} onHide={this.handleClose} animation={false}>
    <Modal.Body>{this.props.modalContent}</Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={this.handleClose}>
              Close
            </Button>
          </Modal.Footer>
        </Modal>
      
    );
  }
  }
  
  export default ModalComp