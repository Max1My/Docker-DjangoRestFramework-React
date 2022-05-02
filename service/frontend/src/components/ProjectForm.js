import React from "react";


class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name:'',
            links_repo:'',
            user: props.users[0]?.id
        }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value,
                [event.target.links_repo]: event.target.value
            }
        )
    }

    handleSubmit(event) {
        this.props.createProject(this.state.name, this.state.user,this.state.links_repo)
        event.preventDefault()
    }

    render(){
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="name">name</label>
                    <input type="text" className="form-control" name="name"
                           value={this.state.name}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="links_repo">links_repo</label>
                    <input type="text" className="form-control" name="links_repo"
                            value={this.state.links_repo}
                            onChange={(event) => this.handleChange(event)}/>
                </div>

                <div className="form-group">
                    <label for="user">user</label>
                    <select name="user" className="form-control" onChange={(event) => this.handleChange(event)}>
                        {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)}
                    </select>
                    {/*<input type="number" className="form-control" name="author"*/}
                    {/*       value={this.state.author}*/}
                    {/*       onChange={(event) => this.handleChange(event)}/>*/}
                </div>
                <input type="submit" className="btn-primary" value='Save'/>
            </form>
        )
    }
}

export default ProjectForm