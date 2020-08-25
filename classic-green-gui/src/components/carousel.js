import React from "react";
import {Carousel} from 'react-bootstrap'
import '../bootstrap.css';

let Addcarousel = (props) => {
    let offerData = ""

    offerData = props.offerItems.map(i => {
            return(
                <Carousel.Item>
                    <Carousel.Caption>
            <h3 style={{"margin-left":"53%",width:"38%",backgroundColor:'pink'}}>{i.offerDescription}</h3>
            {/* <p>{}</p> */}
                </Carousel.Caption> 
                  
            <img src= {i.offerImage} width="30%" height="150px" style={{"margin-left":"21%"}}></img>
                               
            </Carousel.Item>   
            )
    })

return(
    <div>
        <Carousel fade="true" variant="dark">

        {offerData}
        
        </Carousel>    
    </div>
    );

}

export default Addcarousel



