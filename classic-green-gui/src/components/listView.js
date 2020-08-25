import React from 'react'
import '../App.css'
import '../bootstrap.css'
import { Container } from "react-bootstrap"
import { NavLink } from 'react-router-dom'
import ItemThumbnail from './thumbnail.js';

 class DisplayItems extends React.Component {
    constructor(props){
        super(props)
        this.state = {
            categoryData:[],
            loaded:false,
        }

    }
    
    displayCategory=this.props.categories.map(category=>{
        return(
            <NavLink to={category.CatName} > {category.CatName}<br/> </NavLink>
        )
    }

    )

    componentDidUpdate=()=>{
        if (this.state.loaded===true){
        this.state.categoryData.map(eactVariant=>{
            console.log("----------------------------in main3",eactVariant)
            return(
                
                <ItemThumbnail contactData = {eactVariant}/>
                )

        }
    

        )
    }
        else{
            return(
                <div></div>
            )
        }
        
        
    }

    componentDidMount(){
        console.log("---------11")
        
        console.log("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        console.log(this.props.data)
        this.props.data.map(item=>{
         return(   
        fetch(`api/queryVariant/?VarientItemName__Name=${item.Name}`)
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(categoryData => {
          console.log("-----------------in main2: ",categoryData); 
          let bb = [...this.state.categoryData]
          this.setState(() => {
            return {
                categoryData,
              loaded: true,
              imagePresent:true
            }
          })
         
          })
         )})
    }        
    

    render(){
        console.log('-------------------in')
        console.log("category data-------------",this.state.categoryData)
        let im = this.state.imagePresent
    return(
        // <Container style={{width:'120%'}}>
        
        <div className="list-items">
            <div className="side-panel">
                {this.displayCategory}
            </div>
            <div className="view-panel">
            
              {im?<ItemThumbnail contactData = {this.state.categoryData[0]}/>:null}
            </div>

        </div>
        
        
        
    )
    }
}


export default DisplayItems 