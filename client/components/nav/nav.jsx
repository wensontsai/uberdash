import React, { Component } from 'react';
import { Link } from 'react-router';

import './nav.scss';

class Nav extends Component {
	render() {
		return (
		    <div className='nav'>
		    	<div className='nav-title'>
		    		<Link className='link' to='/' >Command Center</Link>
		    	</div>
		    	<div className='nav-links'>
		    		<Link className='link' to='/login' >Login</Link>
		    		<Link className='link' to='/dash' >Main</Link>
		    	</div>
		    </div>
	    )
	}
}

export default Nav;
