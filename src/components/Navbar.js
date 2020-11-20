import React from 'react';
import { Navbar,Nav,Form,Button, FormControl } from 'react-bootstrap';

const Navbars = () => {
    return (
        <>
        <Navbar bg="dark" variant="dark" expand="lg">
        <Navbar.Brand href="#home">
            <img
            alt=""
            src="/logo.svg"
            width="30"
            height="30"
            className="d-inline-block align-top"
        />{' '}
            MLH Fellowship
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
            <Nav.Link href="#home">Projects</Nav.Link>
            <Nav.Link href="#link">Batches</Nav.Link>
        </Nav>
        <Form inline>
        <FormControl type="text" placeholder="Search" className="mr-sm-2" />
        <Button variant="outline-success">Search</Button>
        </Form>
    </Navbar.Collapse>
    </Navbar>
        </>
    )
};

export default Navbars;