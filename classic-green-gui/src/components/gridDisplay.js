import * as React from "react"
import { Container } from "react-bootstrap"
import '../App.css'
import { NavLink } from 'react-router-dom'
export let Grid = (props) => {
    
    let getDataItem= props.data.map(item=> {
            return(
                <NavLink className={`item${item.id} gallery-item`} to={item.CatName}><img src={item.CatImg}  className ="gallery-image"  ></img></NavLink> 
            );
    
        })   
    return(
    
        <Container style={{width:"120%"}}>    
            <div className="grid-container">
                 {getDataItem}
          </div>
        </Container>
        
        )
    }

