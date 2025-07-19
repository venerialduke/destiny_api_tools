import axios from 'axios';
import { authService } from './authService';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

class ApiClient {
  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      timeout: 10000,
    });

    // Request interceptor to add auth headers
    this.client.interceptors.request.use(
      (config) => {
        const token = localStorage.getItem('accessToken');
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    // Response interceptor to handle token refresh
    this.client.interceptors.response.use(
      (response) => response,
      async (error) => {
        const originalRequest = error.config;

        // If the error is 401 and we haven't already tried to refresh
        if (error.response?.status === 401 && !originalRequest._retry) {
          originalRequest._retry = true;

          try {
            const refreshToken = localStorage.getItem('refreshToken');
            if (refreshToken) {
              const tokens = await authService.refreshToken(refreshToken);
              
              // Update stored tokens
              localStorage.setItem('accessToken', tokens.accessToken);
              localStorage.setItem('refreshToken', tokens.refreshToken);
              
              // Retry the original request with new token
              originalRequest.headers.Authorization = `Bearer ${tokens.accessToken}`;
              return this.client(originalRequest);
            }
          } catch (refreshError) {
            // Refresh failed, redirect to login
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            localStorage.removeItem('userData');
            window.location.href = '/login';
            return Promise.reject(refreshError);
          }
        }

        return Promise.reject(error);
      }
    );
  }

  // Auth endpoints
  async login() {
    const response = await this.client.get('/auth/login');
    return response.data;
  }

  async exchangeCode(code) {
    const response = await this.client.post('/auth/callback', { code });
    return response.data;
  }

  async refreshTokens(refreshToken) {
    const response = await this.client.post('/auth/refresh', { 
      refresh_token: refreshToken 
    });
    return response.data;
  }

  // User endpoints
  async getUserProfile() {
    const response = await this.client.get('/core/user/profile');
    return response.data;
  }

  async getUserMemberships() {
    const response = await this.client.get('/core/user/memberships');
    return response.data;
  }

  async getCharacters(membershipType, membershipId) {
    const response = await this.client.get(
      `/core/user/characters/${membershipType}/${membershipId}`
    );
    return response.data;
  }

  async getCharacterDetails(membershipType, membershipId, characterId) {
    const response = await this.client.get(
      `/core/user/character/${membershipType}/${membershipId}/${characterId}`
    );
    return response.data;
  }

  async getCharacterEquipment(membershipType, membershipId, characterId) {
    const response = await this.client.get(
      `/core/user/character/${membershipType}/${membershipId}/${characterId}/equipment`
    );
    return response.data;
  }

  async searchPlayer(bungieName, membershipType) {
    const response = await this.client.post(
      `/core/user/search/${membershipType}`,
      { bungie_name: bungieName }
    );
    return response.data;
  }

  // Core endpoints
  async getHealthCheck() {
    const response = await this.client.get('/core/health');
    return response.data;
  }

  async getManifest() {
    const response = await this.client.get('/core/manifest');
    return response.data;
  }

  async getSettings() {
    const response = await this.client.get('/core/settings');
    return response.data;
  }

  // Generic request methods
  async get(url, config = {}) {
    const response = await this.client.get(url, config);
    return response.data;
  }

  async post(url, data = {}, config = {}) {
    const response = await this.client.post(url, data, config);
    return response.data;
  }

  async put(url, data = {}, config = {}) {
    const response = await this.client.put(url, data, config);
    return response.data;
  }

  async delete(url, config = {}) {
    const response = await this.client.delete(url, config);
    return response.data;
  }

  // Error handling helper
  handleError(error) {
    if (error.response) {
      // Server responded with error status
      const message = error.response.data?.error || error.response.data?.message || 'Server error';
      throw new Error(message);
    } else if (error.request) {
      // Request was made but no response received
      throw new Error('Network error - please check your connection');
    } else {
      // Something else happened
      throw new Error(error.message || 'An unexpected error occurred');
    }
  }
}

export const apiClient = new ApiClient();