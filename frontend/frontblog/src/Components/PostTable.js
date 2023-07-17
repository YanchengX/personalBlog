import React from 'react';
import axios from 'axios';

import Posty from './Posty';

import './general.css'

//posttable framework get all post and comment at right post

class PostTable extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
          data: [],
          loading: true,
          error: false
        };
      }
    
      componentDidMount() {
        this.fetchData();
      }
    
      fetchData = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/postlist'); // 將API端點替換為實際的API URL
          this.setState({ data: response.data, loading: false }); // 將資料存入狀態變數
        } catch (error) {
          console.log(error);
          this.setState({ error: true, loading: true});
        }
      }

      render() {
        const { data, loading, error } = this.state;
        
        if (loading) {
          return <div>Loading...</div>;
        }
      
        if (error) {
          return <div>Error occurred while fetching data.</div>;
        }

        return (
          //這邊可以做css
          <div className='postarea'>
            {data.map(item => (
              <Posty key={item.post_id} data={item} token={this.props.token} setToken={this.props.setToken}/>
            ))}
          </div>
        );


      }
}



export default PostTable

