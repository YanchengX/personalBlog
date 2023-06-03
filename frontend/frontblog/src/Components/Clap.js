import React from 'react'
import axios from 'axios'

class Clap extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            clap : this.props.clapcount,
            postid : this.props.id - 1
        };
        this.handleclap = this.handleClap.bind(this);
        this.handleshowclap = this.handleShowClap.bind(this)
    }
    
    handleShowClap = async () => {
        const {postid} = this.state
        try {
          const response = await axios.get(`/clapcount/${postid}`); 
          this.setState({ clap : response.data['clap_count'], });
        } catch (error) {
          console.log(error);
        }
      }
    

    handleClap = (event) =>{
        const {clap, postid} = this.state
        const data = {
            clap_count : clap,
        }
        axios.put(`/clapcount/${postid}`, data)
            .then(response => {
                this.setState({
                    clap : response.data['clap_count'],
                })
            })
            .catch(error => {
              console.error(error.data);
            });
    }
    
    render(){
        return(
            <div>
                <button className='buttons2' onClick={this.handleClap}>Support</button>
                <label className='clapcount' values={this.state.clap} >{this.state.clap}</label>
            </div>
        )
    }

}

export default Clap

