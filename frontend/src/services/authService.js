import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

class AuthService {
  constructor() {
    this.baseURL = `${API_BASE_URL}/auth`;
  }

  async getAuthUrl() {
    try {
      const response = await axios.get(`${this.baseURL}/login`);
      return response.data.auth_url;
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to get auth URL');
    }
  }

  async exchangeCodeForTokens(code) {
    try {
      const response = await axios.post(`${this.baseURL}/callback`, {
        code
      });
      return {
        accessToken: response.data.access_token,
        refreshToken: response.data.refresh_token,
        expiresIn: response.data.expires_in,
        membershipId: response.data.membership_id
      };
    } catch (error) {
      throw new Error(error.response?.data?.error || 'Failed to exchange code for tokens');
    }
  }

  async refreshToken(refreshToken) {
    try {
      const response = await axios.post(`${this.baseURL}/refresh`, {
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
      await axios.post(`${this.baseURL}/logout`);
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