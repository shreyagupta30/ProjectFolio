import React from 'react';
import {Jumbotron, Button} from 'react-bootstrap';

function Homepage() {
    return (
        <>
        <Jumbotron>
            <p>
                xxx Fellows, xxx Countries <br/>
                xxx Batches, xxx Years <br/>
                xxx Open Source Organizations <br/>
                xxx Commits, xxx Pull Requests <br/>
            </p>
            <p>
                <Button variant="primary">Apply Now</Button>
            </p>
        </Jumbotron>
        </>
    );
}

export default Homepage;