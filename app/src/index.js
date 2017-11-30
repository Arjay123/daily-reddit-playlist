var React = require('react');
var ReactDOM = require('react-dom');
import css from './index.css';
import $ from 'jquery';
import 'velocity-animate';

const urlBase = API_URL;

class App extends React.Component {
    render() {
        return(
            <div className="app">
                <PlayerPanel />
            </div>
        )
    }
}

class PlayerPanel extends React.Component {
    constructor(props) {
        super(props);

        this.handleClick = this.handleClick.bind(this);
        this.changeValue = this.changeValue.bind(this);
        this.state = {
            value: "Playlist 1"
        }
    }

    handleClick() {
        $('#foo').velocity({ "left": "-=275px" }, {
            "duration": "fast",
            "complete": this.changeValue
        });
        console.log("hi");
    }

    changeValue(){
        console.log($('#foo').css('left'));
        $('#foo').css({
            'left': '+=550px'
        })
        this.setState({
            value: "Playlist 2"
        });

        $('#foo').velocity({ "left": "-=275px" }, "fast");
    }

    render() {
        return(
            <div className="player-panel">
                <div onClick={this.handleClick} id='foo' className="player-panel-content">
                    <h2>{this.state.value}</h2>
                    <iframe src="https://open.spotify.com/embed?uri=spotify:user:spotify:playlist:3rgsDhGHZxZ9sB9DQWQfuf" width="300" height="380" frameborder="0" allowtransparency="true"></iframe>
                </div>
            </div>
        )
    }
}


ReactDOM.render(<App />, document.getElementById('main'))