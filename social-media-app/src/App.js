import './App.css';
import Home from './pages/home';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ProtectedRoute from './routes/ProtectedRoute';
import Registration from './pages/registration';
import Login from './pages/login';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/register" element={<Registration />} />
                <Route path="/login/" element={<Login />} />
                <Route
                    path="/"
                    element={
                        <ProtectedRoute children={<Home />}></ProtectedRoute>
                    }
                />
            </Routes>
        </Router>
    );
}

export default App;
