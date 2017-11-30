var React = require('react');
var ReactDOM = require('react-dom');
import css from './index.css';
import $ from 'jquery';
import 'velocity-animate';

const urlBase = API_URL;
const userID = USER_ID;

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
            value: "Playlist 1",
            playlistIndex: 0,
            playlists: ["2C3dph3uefzWsFyY033fX9", "3bbn3u9hTsq7JZ8jzatJt6", "3ttgNUPgUQy9BLaOruFGpT"]
        }
    }

    handleClick() {
        $('#foo').velocity({ "left": "-=275px" }, {
            "duration": "fast",
            "complete": this.changeValue
        });
    }

    changeValue(){
        $('#foo').css({
            'left': '+=550px'
        })

        var newIndex = this.state.playlistIndex < this.state.playlists.length-1 ? this.state.playlistIndex+1 : 0;

        this.setState({
            playlistIndex: newIndex
        });

        $('#foo').velocity({ "left": "-=275px" }, "fast");
    }

    render() {
        var playlistSrc = "https://open.spotify.com/embed?uri=spotify:user:" + userID + ":playlist:" + this.state.playlists[this.state.playlistIndex];
        var frame = <iframe src={playlistSrc} width="300" height="380" frameborder="0" allowtransparency="true"></iframe>;
        return(
            <div className="player-panel">
                <div onClick={this.handleClick} id='foo' className="player-panel-content">
                    <h2>{this.state.value}</h2>
                    {frame}
                </div>
            </div>
        )
    }
}


ReactDOM.render(<App />, document.getElementById('main'))