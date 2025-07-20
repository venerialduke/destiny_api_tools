import React from 'react';
import { Navigate } from 'react-router-dom';
import { LogIn, Shield, Zap, Star, ArrowRight } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';

const LoginPage = () => {
  const { login, isAuthenticated, isLoading } = useAuth();

  // Redirect if already authenticated
  if (isAuthenticated) {
    return <Navigate to="/" replace />;
  }

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-lg text-gray-600">Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-md w-full space-y-8">
          <div className="text-center">
            <div className="bg-blue-600 p-4 rounded-full w-20 h-20 mx-auto mb-6">
              <Shield className="w-12 h-12 text-white" />
            </div>
            <h2 className="text-3xl font-bold text-gray-900 mb-2">
              Connect to Bungie.net
            </h2>
            <p className="text-lg text-gray-600">
              Link your Destiny account to access all tools and features
            </p>
          </div>

          <div className="bg-white rounded-2xl shadow-xl p-8">
            <div className="space-y-6">
              {/* Benefits */}
              <div className="space-y-4">
                <div className="flex items-center">
                  <Shield className="w-6 h-6 text-blue-600 mr-3" />
                  <div>
                    <h3 className="font-semibold text-gray-900">Secure Authentication</h3>
                    <p className="text-sm text-gray-600">Official Bungie OAuth 2.0 integration</p>
                  </div>
                </div>
                
                <div className="flex items-center">
                  <Zap className="w-6 h-6 text-green-600 mr-3" />
                  <div>
                    <h3 className="font-semibold text-gray-900">Real-time Access</h3>
                    <p className="text-sm text-gray-600">Live data from your Destiny 2 account</p>
                  </div>
                </div>
                
                <div className="flex items-center">
                  <Star className="w-6 h-6 text-purple-600 mr-3" />
                  <div>
                    <h3 className="font-semibold text-gray-900">Full Tool Access</h3>
                    <p className="text-sm text-gray-600">Unlock all inventory and character management tools</p>
                  </div>
                </div>
              </div>

              {/* Login Button */}
              <button
                onClick={login}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-6 rounded-xl text-lg transition-colors duration-200 flex items-center justify-center group"
              >
                <LogIn className="w-6 h-6 mr-2" />
                Continue with Bungie.net
                <ArrowRight className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform duration-200" />
              </button>

              {/* Privacy Note */}
              <div className="text-center pt-4 border-t border-gray-200">
                <p className="text-xs text-gray-500">
                  We'll redirect you to Bungie.net for secure authentication.
                  <br />
                  Your credentials are never stored on our servers.
                </p>
              </div>
            </div>
          </div>

          {/* Additional Info */}
          <div className="text-center">
            <p className="text-sm text-gray-600">
              Don't have a Bungie.net account?{' '}
              <a 
                href="https://www.bungie.net/en/User/SignUp" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-blue-600 hover:text-blue-800 font-medium"
              >
                Create one here
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;