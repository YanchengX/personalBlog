import React from 'react'
import Clap from './Clap'
import Comment from './Comment'

import './general.css'

class Posty extends React.Component{
    constructor(props){
        super(props);
        this.state = null;
    }
    //貼文內容排版 props -> post content

    render(){
        //clap comment再細分做運算
        return (
            <div key={this.props.data.post_id}>
                
                <div className='userfield'>
                    {this.props.data.author}<br/>
                </div>
                <div className='content'>
                    {this.props.data.content}<br/>
                </div>
                                    
                <div className=''> 
                    <Clap id ={this.props.data.post_id} clapcount= {this.props.data.clap_count}/>
                </div>
                
                <br/>
                
                <div className='commentlist'>
                    <Comment id ={this.props.data.post_id} comment={this.props.data.commentat} 
                                    token={this.props.token} setToken={this.props.setToken}/>
                </div>
                <div className='line'>
                </div>
            </div>
        )
    }
}


export default Posty

