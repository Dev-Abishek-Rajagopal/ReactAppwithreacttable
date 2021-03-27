import React from 'react';
import '../style.css';
import axios from 'axios';

class Search extends React.Component {

    constructor(props){

        super(props);
        this.state =  {
            query: '',
            results: {},
            loading: false,
            message: ''
        }
        this.cancel = '';
    }

    fetchSearchResults = (  query ) => {
		const searchUrl = `api=${query}`;

		if( this.cancel ) {
			this.cancel.cancel();
		}

		this.cancel = axios.CancelToken.source();

		axios.get( searchUrl, {
			cancelToken: this.cancel.token
		} )
			.then( res => {
				console.warn(res);
			} )
            .catch( error => {
				if ( axios.isCancel(error) || error ) {
					this.setState({
						loading: false,
						message: 'Failed to fetch the data. Please check network'
					})
				}
			} )

	};


    handleonInputChange = ( event ) => {
        
        // query store
        const query = event.target.value;
        //setting state
        this.setState({ query: query, loading: true,message: '' }, () => this.fetchSearchResults(query) );
    };

	render() {

        //get query here in render
        const { query } = this.state.query;

		return (
			<div className="container">
                {/* Heading */}
                <h2 className = "heading"> Search your Agri Business</h2>
                {/* Search Box */}
                <label className="search-label" htmlFor="search-input">
				<input
                    name = "query"
					type="text"
					value= { query }
					id="search-input"
					placeholder="Search..."
                    onChange={this.handleonInputChange}
                />
				<i className="fa fa-search search-icon" aria-hidden="true"/>
			</label>
            </div>
		)
	}
}

export default Search