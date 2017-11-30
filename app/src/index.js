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

        this.changeValue = this.changeValue.bind(this);
        this.prevClick = this.prevClick.bind(this);
        this.nextClick = this.nextClick.bind(this);
        this.playlistChanged = this.playlistChanged.bind(this);

        this.state = {
            value: "Playlist 1",
            playlistIndex: 0,
            playlists: ["2C3dph3uefzWsFyY033fX9", "3bbn3u9hTsq7JZ8jzatJt6", "3ttgNUPgUQy9BLaOruFGpT"],
            frameHeight: 200,
            frameWidth: 200
        }
    }


    componentDidMount() {
        console.log($('.player-panel').height());
        console.log($('.player-panel').width());

        this.setState({
            frameHeight: $('.player-panel').height() - 100,
            frameWidth: $('.player-panel').width() - 50
        })
    }


    prevClick() {
        var index = this.state.playlistIndex > 0 ? this.state.playlistIndex-1 : this.state.playlists.length-1;
        this.playlistChanged(index);
    }


    nextClick() {
        var index = this.state.playlistIndex < this.state.playlists.length-1 ? this.state.playlistIndex+1 : 0;
        this.playlistChanged(index);
    }


    playlistChanged(index) {
        $('#foo').velocity({ "left": "-=275px" }, {
            "duration": "fast",
            "complete": this.changeValue(index)
        });
    }


    changeValue(index){
        $('#foo').css({
            'left': '+=550px'
        });

        this.setState({
            playlistIndex: index
        });

        $('#foo').velocity({ "left": "-=275px" }, "fast");
    }

    render() {
        var playlistSrc = "https://open.spotify.com/embed?uri=spotify:user:" + userID + ":playlist:" + this.state.playlists[this.state.playlistIndex];
        var frame = <iframe src={playlistSrc} width={this.state.frameWidth} height={this.state.frameHeight} frameborder="0" allowtransparency="true"></iframe>;
        return(
            <div className="player-panel">
                <div id='foo' className="player-panel-content">
                    <h2>{this.state.value}</h2>
                    {frame}
                    <div className="controls">
                        <button onClick={this.prevClick}>left</button>
                        <button onClick={this.nextClick}>right</button>
                    </div>
                </div>
            </div>
        )
    }
}


ReactDOM.render(<App />, document.getElementById('main'))