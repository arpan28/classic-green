import React from 'react';
import logo from './logo.svg';
import './App.css';
import BackImg from './ui-img/backGroundImg.jpg'
import {Navigation} from './components/navigation'
import Carousels from './components/carousel' 
import VideoThumbnail from 'react-video-thumbnail'; // use npm published version

import {Button} from 'react-bootstrap';
import ItemThumbnail from './components/thumbnail';
// import BannerCreator from './components/banner';
import {Grid} from './components/gridDisplay';
import LoginPage from './components/login'
import { BrowserRouter as Router ,Route,Switch} from 'react-router-dom'
import { Link} from 'react-router-dom'	
// import ClassicGreen from './img/logo_icon-removebg-preview2.png '
import ItemDisplay from './components/displayItems'


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data1: [],
      data2: [],
      data3: [],
	  data4: [],
	  data5: [],
      loaded: false,
      placeholder: "Loading"
    };
  }


  componentDidMount() {
    fetch("/api/items/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data1 => {
        this.setState(() => {
          return {
            data1,
            loaded: true
          };
        });
      });
      fetch("/api/category/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data2 => {
        this.setState(() => {
          return {
            data2,
            loaded: true
          };
        });
      });
      fetch("/api/variant/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data3 => {
        this.setState(() => {
          return {
            data3,
            loaded: true
          };
        });
      });
      fetch("/api/offers/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data4 => {
        this.setState(() => {
          return {
            data4,
            loaded: true
          };
        });
	  });
	  fetch("/api?Category=Plant&db=category")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data5 => {
        this.setState(() => {
          return {
            data5,
            loaded: true
          };
        });
      });
  }
  
  
  render() {
    let sectionStyle = {
      width: "100%",
      height: "2000px",
      backgroundImage: "url(" + { BackImg } + ")"
    };
	
    let plantsData = this.state.data2.map(contact => {
		
      return (
      <ItemThumbnail contactData = {contact}/>
     
      );
	})
	
	let CatData = this.state.data2.map(category =>{
		return(
		<Route
		path={`/${category.CatName}`}
		render={(props) => <ItemDisplay {...props} key2='CatName' catName={category.CatName} allCat={this.state.data2} />}

	/>)
	}

	)

	
    return (

			<Router>
				<div className="style-app" style={sectionStyle}>

						<Navigation mainState = {this.state}/>
						<br />
						<br />
						<Carousels offerItems = {this.state.data4}/>
						<br />
					

				
				<Switch>
						<Route
							path='/'
							render={(props) =><Grid {...props} data={this.state.data2} />}
							exact
						/>
						{CatData}
				</Switch>
			</div>			
			</Router>


				); 


{/* <Grid /> */}
{/* {giftsData} */}
{/* <BannerCreator /> */}
{/* <LoginPage /> */}
{/* <img src={ClassicGreen}/> */}
     
      

      
         
  }

}

export default App;
