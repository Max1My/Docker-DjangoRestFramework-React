import React from 'react'
import {Link, useParams} from "react-router-dom";


const ToDoItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.project.name}</td>
            <td>{item.user.name}</td>
            <td>{item.text}</td>
        </tr>
    )
}

const ToDoList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>PROJECT</th>
                <th>USER</th>
                <th>COMMIT</th>
            </tr>
            {items.map((item) => <ToDoItem item={item}/>)}
        </table>
    )
}



export default ToDoList