import React from 'react'
import {Link} from "react-router-dom";


const UserItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.username}</td>
            <td>{item.email}</td>
        </tr>
    )
}
const UserList = ({items}) => {
    return (
        <div>
        <table>
            <tr>
                <th>ID</th>
                <th>USERNAME</th>
                <th>EMAIL</th>
                <th></th>
            </tr>
            {items.map((item) => <UserItem item={item}/>)}
        </table>
        </div>
    )
}



export default UserList