import React from 'react'
import axios from 'axios'

import './general.css'

class MenuTable extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            username : "",
            password : "",
            loginstatus : false,
        }
        this.username = this.handleUsername.bind(this);
        this.password = this.handlepassowrd.bind(this);
        this.registerclick = this.handleRegister.bind(this);
        this.loginclick = this.handelLogin.bind(this);

    };
    componentDidUpdate(){
      const {loginstatus} = this.state
      if (loginstatus === true){
        localStorage.setItem('token',this.props.token);
      }else{
        localStorage.removeItem('token',this.props.token);
      }
    }
    
    handleUsername = (event) => {
        this.setState({"username": event.target.value});
    };

    handlepassowrd = (event) => {
        this.setState({"password": event.target.value});
    };

    handelLogin = (event) => {
        //get username password, return status -> refresh view -> get token to see post

        const {username, password} = this.state;
        const data = {
            username : username,
            password : password,
        };
        axios.post('vmblog-388622.de.r.appspot.com/login', data)
        .then(response => {
            this.setState({
                loginstatus : true,
            })
            this.props.setToken(response.data['token'])
        })
        .catch(error => {
          console.error(error);
          alert("invalid input")
        });
    };

    handleRegister = (event) => {
        const {username, password} = this.state;
        const data = {
            username : username,
            password : password,
        };
        
        axios.post('vmblog-388622.de.r.appspot.com/register', data)
        .then(response => {
          //處理註冊完成
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
          alert("invalid input")
        });
    };

    handelLogout = (event) => {
        axios.post(
          'vmblog-388622.de.r.appspot.com/logout', {},
          {
            headers: {
              Authorization: `Bearer ${this.props.token}`,
            },
          }
        )
          .then(response => {
            this.setState({
              loginstatus: false,
              username: '',
              password: '',
            });
            this.props.setToken('')
            console.log(response.data);
            localStorage.removeItem('token')
          })
          .catch(error => {
            console.error(error.data);
          });
      };
      
    render(){
        const { username, password, loginstatus } = this.state;
        
        if (loginstatus){
            return(
                <div>
                    <h1>Salve!,{username}</h1>
                    <button onClick={this.handelLogout}>Logout</button>
                </div>
            )
        }
        return (
          <div className='loginarea'>
                <input className='input1' name='user' type="text" value={username} onChange={this.handleUsername} />
                <input className='input1' name='pwd' type="password" value={password} onChange={this.handlepassowrd} />
                <button className='buttons1' variant="primary" onClick={this.handelLogin}>Login</button>
                <button className='buttons1' variant="info" onClick={this.handleRegister}>Register</button>

                {localStorage.removeItem('token')}  
            </div>
            
        )
    }
}

export default MenuTable

