import React from 'react';
import Card from 'react-bootstrap/Card';
import '../bootstrap.css';


let handleOnItemClictEvent = () => {
    console.log("called");
  }
let ItemThumbnail = (props)=>{
    console.log("######################3")
    console.log("----------------------------props: ",props)
    return(
        // <div className = "style-item-thumbnail" onClick={handleOnItemClictEvent} >
        //      <Card style={{ width: '12rem'}} >
        //      <Card.Img variant="top" src={props.contactData.image} />
        //         <Card.Body>
        //             <Card.Title as="h6" >{props.contactData.plantName}</Card.Title>
        //             <Card.Text>
        //                 {props.contactData.description}
        //             </Card.Text>
            
        //         </Card.Body>
        //      </Card>
        // </div>
        <div className="gallery">
            <a target="_blank" href="img_5terre.jpg">
                <img src={props.contactData.VarientItemImage} alt="Cinque Terre" width="600" height="400"/>
            </a>
            <div className="desc">{props.contactData.VarientItemName}</div>
        </div>
        )

    

}


export default ItemThumbnail;