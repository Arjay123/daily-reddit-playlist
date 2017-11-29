var React = require('react');
var ReactDOM = require('react-dom');
import css from './index.css';

const urlBase = API_URL;

class People extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            data: [{"test": "test"}]
        }
    }

    load() {
        $.ajax({
            url: API_URL + "persons",
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data.results});
                console.log(data)
            }.bind(this),
            error: function(error){
                this.setState({data: []})
                console.log("error")
            }.bind(this)
        })
    }

    componentDidMount() {
        this.load();
    }

    render() {

        var data_render = <p className="error">Error: data not loaded</p>
        if(this.state.data){
            data_render = this.state.data.map((i, j) =>
                <Person key={j} name={i.name} game={i.fav_game} age={i.age} />
            );
        }

        return (
            <div className="people">
                {data_render}
            </div>
        )
    }
}

class Person extends React.Component {
    render(){
        return(
            <div className="person">
                <h3>{this.props.name}</h3>
                <h4>Age {this.props.age}</h4>
                <p>Favorite Game: {this.props.game}</p>
            </div>
        )
    }
}

class App extends React.Component {
    render() {
        return(
            <div className="app">
                <Header />
                <div className="content">
                    <h1>Data from API call</h1>
                    <People />
                </div>
            </div>
        )
    }
}


class Header extends React.Component {
    render() {
        return(
            <header className="hdr">
                <h1>django-react-playground</h1>
            </header>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('container'))