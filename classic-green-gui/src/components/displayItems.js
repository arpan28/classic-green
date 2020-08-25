import React from 'react'
import DisplayItems from './listView'


class ItemDisplay extends React.Component{
    constructor(props){
        super();

        this.state={
            cateoryData:[],
            loaded: false,
            dataPresent:false
        }

    }

    componentDidMount(){
        // fetch(`query/?dataDict={"db":"Item","foreignKey":"","key":"${this.props.key2}","query":"${this.props.catName}"}`)
        fetch(`api/queryItem/?Category__${this.props.key2}=${this.props.catName}`)
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              console.log("--------------display itm ki fetch api")
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(cateoryData => {
          console.log("=====catData: ",cateoryData)  
          this.setState(() => {
            return {
                cateoryData,
              loaded: true,
              dataPresent:true
            };
          });
        });

    }

    render(){
      let ab = this.state.dataPresent
      console.log("-------------------------prev in display items ",this.state.cateoryData)

        return(
          <div>

          {ab?<DisplayItems categories={this.props.allCat} data={this.state.cateoryData} />:null}
          </div> 
        )
    }
 

    
        
}

export default  ItemDisplay