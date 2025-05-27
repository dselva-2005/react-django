import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import useUserActions from '../../hooks/user.actions';  

const RegistrationForm = () => {
    const navigate = useNavigate();
    const userAction = useUserActions();

    const [form, setForm] = useState({
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        password: '',
        bio: '',
    });

    const [validated, setValidated] = useState(false);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = (event) => {
        event.preventDefault();
        const registrationForm = event.currentTarget;

        setValidated(true);

        if (registrationForm.checkValidity() === false) {
            event.stopPropagation();
            return;
        }

        setLoading(true);
        setError('');

        const data = {
            first_name: form.first_name,
            last_name: form.last_name,
            username: form.username,
            email: form.email,
            password: form.password,
            bio: form.bio,
        };

        userAction.register(data).catch((err) => {
                const apiError =
                    err.response?.data?.detail ||
                    'Registration failed. Please try again.';
                setError(apiError);
            })
            .finally(() => setLoading(false));
    };

    return (
        <Form
            id="registration-form"
            className="border p-4 rounded"
            noValidate
            validated={validated}
            onSubmit={handleSubmit}
        >
            <Form.Group className="mb-3">
                <Form.Label>First Name</Form.Label>
                <Form.Control
                    value={form.first_name}
                    onChange={(e) =>
                        setForm({ ...form, first_name: e.target.value })
                    }
                    required
                    type="text"
                    placeholder="Enter first name"
                />
                <Form.Control.Feedback type="invalid">
                    This field is required.
                </Form.Control.Feedback>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label>Last Name</Form.Label>
                <Form.Control
                    value={form.last_name}
                    onChange={(e) =>
                        setForm({ ...form, last_name: e.target.value })
                    }
                    required
                    type="text"
                    placeholder="Enter last name"
                />
                <Form.Control.Feedback type="invalid">
                    This field is required.
                </Form.Control.Feedback>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label>Username</Form.Label>
                <Form.Control
                    value={form.username}
                    onChange={(e) =>
                        setForm({ ...form, username: e.target.value })
                    }
                    required
                    type="text"
                    placeholder="Enter username"
                />
                <Form.Control.Feedback type="invalid">
                    This field is required.
                </Form.Control.Feedback>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label>Email address</Form.Label>
                <Form.Control
                    value={form.email}
                    onChange={(e) =>
                        setForm({ ...form, email: e.target.value })
                    }
                    required
                    type="email"
                    placeholder="Enter email"
                />
                <Form.Control.Feedback type="invalid">
                    Please provide a valid email.
                </Form.Control.Feedback>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label>Password</Form.Label>
                <Form.Control
                    value={form.password}
                    minLength={8}
                    onChange={(e) =>
                        setForm({ ...form, password: e.target.value })
                    }
                    required
                    type="password"
                    placeholder="Password"
                />
                <Form.Control.Feedback type="invalid">
                    Please provide a valid password (at least 8 characters).
                </Form.Control.Feedback>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label>Bio</Form.Label>
                <Form.Control
                    value={form.bio}
                    onChange={(e) => setForm({ ...form, bio: e.target.value })}
                    required
                    as="textarea"
                    rows={3}
                    placeholder="A simple bio ... (Optional)"
                />
            </Form.Group>

            {error && (
                <div className="text-danger mb-3">
                    <p>{error}</p>
                </div>
            )}

            <Button variant="primary" type="submit" disabled={loading}>
                {loading ? 'Submitting...' : 'Submit'}
            </Button>
        </Form>
    );
};

export default RegistrationForm;
