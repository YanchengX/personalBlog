import MenuTable from "./MenuTable";
import InfoTable from "./InfoTable";
import PostTable from './PostTable'
import React from 'react'

import './general.css';

class Blog extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            tokenshare : '',
        }
    }
    
    setToken = (newState) =>{
        this.setState({
            tokenshare : newState
        })
    }

    render(){
        return (
                <body className="back">
                    <div className="menubar">
                        <MenuTable token={this.state.tokenshare} setToken={this.setToken}/>
                    </div>
            
                    <InfoTable token={this.state.tokenshare} setToken={this.setToken}/>
                    <PostTable token={this.state.tokenshare} setToken={this.setToken}/>
                </body>
        )
    }
}


export default Blog;
