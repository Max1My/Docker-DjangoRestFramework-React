import React from 'react'
import ProjectList from "./components/Project";
import UserList from "./components/User";
import ProjectForm from "./components/ProjectForm";
import ProjectUserList from "./components/ProjectUser";
import LoginForm from './components/Auth.js'
import {BrowserRouter, Route, Switch, Redirect, Link} from 'react-router-dom'
import axios from 'axios'
import Cookies from 'universal-cookie';

const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'projects': [],
            'users': [],
            'token': ''
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://151.248.118.143:8000/api-token-auth/', {
            username: username,
            password: password
        })
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }



    deleteProject(id) {
        axios.delete(`http://151.248.118.143:8000/api/projects/${id}`)
            .then(response => {
                this.setState({
                    projects: this.state.projects.filter((item) => item.id !==
                        id)
                })
            }).catch(error => console.log(error))
    }

    createProject(name,user,links_repo) {
        const headers = this.get_headers()
        const data = {name: name, user: user, links_repo:links_repo}
        axios.post(`http://151.248.118.143:8000/api/projects/`,data,{headers})
            .then(response => {
                let newProject = response.data
                const user = this.state.users.filter((item) => item.id === newProject.user)[0]
                newProject.user = user
                this.setState({projects: [...this.state.projects, newProject]})
            }).catch(error => console.log(error))
    }


    load_data() {
        const headers = this.get_headers()
        axios.get('http://151.248.118.143:8000/api/users/', {headers})
            .then(response => {
                this.setState({users: response.data})
            }).catch(error => console.log(error))
        axios.get('http://151.248.118.143:8000/api/projects/', {headers})
            .then(response => {
                this.setState({projects: response.data})
            }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })
    }



    componentDidMount() {
        this.get_token_from_storage()
        this.load_data()
    }

    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link> }
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList
                            items={this.state.users}/>}/>
                        <Route exact path='/projects/create' component={() => <ProjectForm users={this.state.users} createProject={(name,user,links_repo) => this.createProject(name, user,links_repo)}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList
                            items={this.state.projects} deleteProject={(id) => this.deleteProject(id)}/>}/>
                        <Route path="/user/:id">
                            <ProjectUserList items={this.state.projects}/>
                        </Route>
                        <Redirect from='/users' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App
