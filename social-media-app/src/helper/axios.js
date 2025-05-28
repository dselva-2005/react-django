import axios from 'axios';
import createAuthRefreshInterceptor from 'axios-auth-refresh';

const axiosService = axios.create({
    baseURL: 'http://localhost:8000', // fixed
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add the Authorization header before every request
axiosService.interceptors.request.use((config) => {
    const authData = JSON.parse(localStorage.getItem('auth'));
    if (authData && authData.access) {
        config.headers.Authorization = `Bearer ${authData.access}`;
    }
    return config;
});

// Handle response errors
axiosService.interceptors.response.use(
    (response) => Promise.resolve(response),
    (error) => Promise.reject(error)
);

// Refresh logic for 401 responses
const refreshAuthLogic = async (failedRequest) => {
    try {
        const authData = JSON.parse(localStorage.getItem('auth'));
        if (!authData || !authData.refresh) {
            throw new Error('No refresh token available');
        }

        const resp = await axios.post('/api/auth/refresh', {"refresh":authData.refresh}, {
            baseURL: 'http://localhost:8000',
        });

        const { access, refresh: newRefresh } = resp.data;

        // Update the failed request's authorization header
        failedRequest.response.config.headers[
            'Authorization'
        ] = `Bearer ${access}`;

        // Save the new tokens
        localStorage.setItem(
            'auth',
            JSON.stringify({ access, refresh: newRefresh })
        );

        return Promise.resolve();
    } catch (error) {
        localStorage.removeItem('auth');
        return Promise.reject(error);
    }
};

// Attach the refresh logic to axiosService
createAuthRefreshInterceptor(axiosService, refreshAuthLogic);

// Fetcher for SWR (simple GET)
export function fetcher(url) {
    return axiosService.get(url).then((res) => res.data);
}

export default axiosService;
