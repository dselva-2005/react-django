import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function useUserActions() {
    const navigate = useNavigate();
    const baseURL = 'http://localhost:8000/api';

    function setUserData(data) {
        localStorage.setItem(
            'auth',
            JSON.stringify({
                access: data.access,
                refresh: data.refresh,
                user: data.user,
            })
        );
    }

    function login(data) {
        return axios.post(`${baseURL}/auth/login`, data).then((res) => {
            setUserData(res.data);
            navigate('/');
        });
    }

    function register(data) {
        // Implement registration logic, e.g.:
        return axios.post(`${baseURL}/auth/register`, data).then((res) => {
            // You might auto-login or navigate after registration here
            navigate('/login');
        });
    }

    function logout() {
        localStorage.removeItem('auth');
        navigate('/login');
    }

    function getUser() {
        const auth = JSON.parse(localStorage.getItem('auth'));
        return auth?.user || null;
    }

    function getAccessToken() {
        const auth = JSON.parse(localStorage.getItem('auth'));
        return auth?.access || null;
    }

    function getRefreshToken() {
        const auth = JSON.parse(localStorage.getItem('auth'));
        return auth?.refresh || null;
    }

    return {
        login,
        register,
        logout,
        getUser,
        getAccessToken,
        getRefreshToken,
    };
}

export default useUserActions;
