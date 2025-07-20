import { apiClient } from './apiClient';

class UserService {
  constructor() {
    this.apiClient = apiClient;
  }

  async getUserProfile() {
    try {
      return await this.apiClient.getUserProfile();
    } catch (error) {
      this.apiClient.handleError(error);
    }
  }

  async getUserMemberships() {
    try {
      return await this.apiClient.getUserMemberships();
    } catch (error) {
      this.apiClient.handleError(error);
    }
  }

  async getCharacters(membershipType, membershipId) {
    try {
      return await this.apiClient.getCharacters(membershipType, membershipId);
    } catch (error) {
      this.apiClient.handleError(error);
    }
  }

  async getCharacterDetails(membershipType, membershipId, characterId) {
    try {
      return await this.apiClient.getCharacterDetails(membershipType, membershipId, characterId);
    } catch (error) {
      this.apiClient.handleError(error);
    }
  }

  async getCharacterEquipment(membershipType, membershipId, characterId) {
    try {
      return await this.apiClient.getCharacterEquipment(membershipType, membershipId, characterId);
    } catch (error) {
      this.apiClient.handleError(error);
    }
  }

  async searchPlayer(bungieName, membershipType) {
    try {
      return await this.apiClient.searchPlayer(bungieName, membershipType);
    } catch (error) {
      this.apiClient.handleError(error);
    }
  }
}

export const userService = new UserService();