import React from 'react';
import { randomAvatar } from '../utils/randomAvatar';
import { Nav, NavDropdown, Navbar, Container, Image } from 'react-bootstrap';
import useUserActions from '../hooks/user.actions';

function Navigationbar() {
    const handleLogout = useUserActions().logout;

    return (
        <Navbar bg="primary" variant="dark">
            <Container>
                <Navbar.Brand className="fw-bold" href="#home">
                    postgram
                </Navbar.Brand>
                <Navbar.Collapse className="justify-content-end">
                    <Nav>
                        <NavDropdown
                            title={
                                <Image
                                    src={randomAvatar()}
                                    roundedCircle
                                    width={36}
                                    height={36}
                                />
                            }
                        >
                            <NavDropdown.Item href="#">
                                Profile
                            </NavDropdown.Item>
                            <NavDropdown.Item onClick={handleLogout}>
                                Logout
                            </NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default Navigationbar;
