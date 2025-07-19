import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

// Create a separate axios instance for auth requests (no interceptors)
const authClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
});

class AuthService {
  constructor() {
    this.baseURL = `${API_BASE_URL}/auth`;
  }

  async getAuthUrl() {
    try {
      const response = await authClient.get('/auth/login');
      return response.data.auth_url;
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to get auth URL');
    }
  }

  async exchangeCodeForTokens(code) {
    try {
      const response = await authClient.post('/auth/callback', {
        code
      });
      return {
        accessToken: response.data.access_token,
        refreshToken: response.data.refresh_token,
        expiresIn: response.data.expires_in,
        userData: response.data.user_data
      };
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to exchange code for tokens');
    }
  }

  async refreshToken(refreshToken) {
    try {
      const response = await authClient.post('/auth/refresh', {
        refresh_token: refreshToken
      });
      return {
        accessToken: response.data.access_token,
        refreshToken: response.data.refresh_token,
        expiresIn: response.data.expires_in
      };
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to refresh token');
    }
  }

  async logout() {
    try {
      await authClient.post('/auth/logout');
    } catch (error) {
      // Logout can fail but we should still clear local storage
      console.error('Logout request failed:', error);
    }
  }

  getAuthHeaders(token) {
    return {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    };
  }
}

export const authService = new AuthService();