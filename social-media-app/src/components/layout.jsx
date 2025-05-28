import React from 'react';
import Navigationbar from './navbar';

function Layout(props) {
    return (
        <div>
            <Navigationbar />
            <div className="container m-5">{props.children}</div>
        </div>
    );
}

export default Layout;
