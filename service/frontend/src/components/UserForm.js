import React from "react";


class UserForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username:'',
            project: props.projects[0]?.id
        }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.username]: event.target.value
            }
        )
    }

    handleSubmit(event) {
        this.props.createUser(this.state.username, this.state.project)
        event.preventDefault()
    }

    render(){
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="username">Username</label>
                    <input type="text" className="form-control" name="username"
                           value={this.state.username}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <div className="form-group">
                    <label for="project">project</label>
                    <select name="project" className="form-control" onChange={(event) => this.handleChange(event)}>
                        {this.props.projects.map((item) => <option value={item.id}>{item.username}</option>)}
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

export default UserForm