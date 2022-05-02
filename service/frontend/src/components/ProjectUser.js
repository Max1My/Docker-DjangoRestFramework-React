import React from 'react'
import { useParams } from 'react-router-dom'

const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.user_test.username}</td>
        </tr>
    )
}

const ProjectUserList = ({items}) => {
    let { id } = useParams();
    let filtered_items = items.filter((item) => item.user_test.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>PROJECT</th>
                <th>USERNAME</th>
            </tr>
            {filtered_items.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}

export default ProjectUserList