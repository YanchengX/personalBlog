import React from 'react'
import axios from 'axios'
class Comment extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            //get原本留言data
            cid : this.props.comment.comment_id,
            content : this.props.comment.content,
            postlocate : this.props.id,
            user : this.props.comment.user,

            //處理新留言+判斷哪位使用者
            userid : 0,
            new_comment : '',

            //留言區更新
            comarea : [],
        }
        this.handlecomment = this.handleComment.bind(this)
    }

    componentDidUpdate(prevState){
        const {userid} = this.state
        if (userid === 0){
            this.findUserName()
        }
    }
    
    //刷新留言 重新get postlist 或是直接加一個label上去

    handleAddComment = (data) => {
        const newComment = data['content'] // 新增的留言內容，這裡只是示範用
        this.setState(prevState => ({
            comarea: [...prevState.comarea, newComment],
        }));
      };


    //當menu登入之後同時成立的token並不會馬上get到東西而要透過update來處理得到token
    //得知token意味登入狀態就可以顯示留言，否則不顯示(判斷login)


    handleComment = (event) =>{
        this.setState({"new_comment": event.target.value});
    }

    findUserName = () =>{
        //get username
        if (this.props.token !== ''){
            axios.get(
                'vmblog-388622.de.r.appspot.com/user',
                {
                  headers: {
                    Authorization:  `Bearer ${this.props.token}`,
                  },
                }
              )
                .then(response => {
                    this.setState({
                        userid: response.data["id"],
                  })
    
                })
                .catch(error => {
                  console.error(error)
                })
        }
    }
    
    SendOnClick = (event) =>{
        const {new_comment, postlocate, userid} = this.state
        const data = {
            content: new_comment,
            user: userid,
            post_locate: postlocate
        }
        const jsonData = JSON.stringify(data);
        console.log(jsonData)
        // post commentlist
        axios.post('vmblog-388622.de.r.appspot.com/commentlist', jsonData,{
            headers: {
                'Content-Type': 'application/json',
              },
        })
        .then(response =>{
            //更新留言 返回預設
            this.setState({
               new_comment : '', 
            })
            this.handleAddComment(data)
        })
        .catch(error =>{
            console.error(error)
            alert('error')
            this.setState({
                new_comment : '', 
             })
        })
        
    }

    render(){
        //comment 結構 render問題細分
        const {new_comment, comarea} = this.state
        return(
            <div >
                {this.props.comment.map(item => (
                <div className='comment' key={item.comment_id}>
                    {item.content}
                </div>
                ))}

                {comarea.map((comment, index) => (
                        <div className='comment' key={index}>{comment}</div>
                    ))}

                <textarea className='textare'  value={new_comment} onChange={this.handleComment}></textarea>
                <button className='buttons2' onClick={this.SendOnClick}>送出</button>
            </div>
        )
    }
}

export default Comment
