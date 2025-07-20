import React, { useEffect, useState, useRef } from 'react';
import { Navigate, useSearchParams } from 'react-router-dom';
import { CheckCircle, XCircle, Loader } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';

const CallbackPage = () => {
  const [searchParams] = useSearchParams();
  const { handleCallback, isAuthenticated } = useAuth();
  const [status, setStatus] = useState('processing'); // 'processing', 'success', 'error'
  const [error, setError] = useState(null);
  const hasProcessed = useRef(false);

  useEffect(() => {
    const processCallback = async () => {
      // Use ref to prevent duplicate processing
      if (hasProcessed.current) {
        console.log('DEBUG: Already processed, skipping');
        return;
      }
      hasProcessed.current = true;
      
      try {
        const code = searchParams.get('code');
        const state = searchParams.get('state');
        const error = searchParams.get('error');
        const errorDescription = searchParams.get('error_description');
        
        console.log('DEBUG: Callback URL params:', {
          code: code?.substring(0, 10) + '...',
          state: state?.substring(0, 10) + '...',
          error,
          errorDescription,
          fullParams: Object.fromEntries(searchParams.entries())
        });

        // Check for OAuth errors
        if (error) {
          const fullError = errorDescription ? `${error}: ${errorDescription}` : error;
          setStatus('error');
          setError(`Authentication failed: ${fullError}`);
          return;
        }

        // Check for required parameters
        if (!code) {
          setStatus('error');
          setError('Missing authorization code');
          return;
        }

        // Verify state parameter (CSRF protection) - only if state was provided
        const storedState = localStorage.getItem('oauth_state');
        if (state && storedState && state !== storedState) {
          setStatus('error');
          setError('Invalid state parameter - possible CSRF attack');
          return;
        }

        // Clear stored state if it exists
        if (storedState) {
          localStorage.removeItem('oauth_state');
        }

        // Process the callback
        const success = await handleCallback(code);
        
        if (success) {
          setStatus('success');
          // Redirect will happen automatically via Navigate component
        } else {
          setStatus('error');
          setError('Failed to exchange authorization code for tokens');
        }
      } catch (err) {
        console.error('Callback processing error:', err);
        setStatus('error');
        setError(err.message || 'An unexpected error occurred');
      }
    };

    processCallback();
  }, [searchParams, handleCallback]);

  // Redirect to home page if already authenticated
  if (isAuthenticated && status === 'success') {
    return <Navigate to="/" replace />;
  }
  
  // Also redirect if already authenticated (e.g., on page refresh)
  if (isAuthenticated && status === 'processing') {
    return <Navigate to="/" replace />;
  }

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center">
      <div className="max-w-md w-full bg-white rounded-2xl shadow-xl p-8 text-center">
        {status === 'processing' && (
          <>
            <div className="mb-6">
              <Loader className="w-16 h-16 text-blue-600 mx-auto animate-spin" />
            </div>
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              Completing Authentication
            </h2>
            <p className="text-gray-600">
              Processing your Bungie.net authentication...
            </p>
          </>
        )}

        {status === 'success' && (
          <>
            <div className="mb-6">
              <CheckCircle className="w-16 h-16 text-green-600 mx-auto" />
            </div>
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              Authentication Successful!
            </h2>
            <p className="text-gray-600 mb-6">
              Your Bungie.net account has been successfully linked.
              Redirecting you to the dashboard...
            </p>
            <div className="animate-pulse">
              <div className="h-2 bg-green-200 rounded-full">
                <div className="h-2 bg-green-600 rounded-full animate-pulse"></div>
              </div>
            </div>
          </>
        )}

        {status === 'error' && (
          <>
            <div className="mb-6">
              <XCircle className="w-16 h-16 text-red-600 mx-auto" />
            </div>
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              Authentication Failed
            </h2>
            <p className="text-gray-600 mb-6">
              {error || 'An error occurred during authentication.'}
            </p>
            <div className="space-y-3">
              <button
                onClick={() => window.location.href = '/login'}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-4 rounded-lg transition-colors duration-200"
              >
                Try Again
              </button>
              <button
                onClick={() => window.location.href = '/'}
                className="w-full bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium py-3 px-4 rounded-lg transition-colors duration-200"
              >
                Return Home
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default CallbackPage;