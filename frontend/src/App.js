import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { Toaster } from 'react-hot-toast';

// Context providers
import { AuthProvider } from './contexts/AuthContext';
import { ThemeProvider } from './contexts/ThemeContext';

// Layout components
import Layout from './components/layout/Layout';
import ProtectedRoute from './components/shared/ProtectedRoute';

// Pages
import HomePage from './pages/HomePage';
import LoginPage from './pages/auth/LoginPage';
import CallbackPage from './pages/auth/CallbackPage';
import CharacterDashboard from './pages/CharacterDashboard';
import ExplorationPage from './pages/ExplorationPage';
import ManifestExplorer from './pages/ManifestExplorer';

// Styles
import './App.css';

// Create a client for React Query
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 3,
      staleTime: 5 * 60 * 1000, // 5 minutes
      cacheTime: 10 * 60 * 1000, // 10 minutes
    },
  },
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider>
        <AuthProvider>
          <Router>
            <div className="App">
              <Layout>
                <Routes>
                  {/* Public routes */}
                  <Route path="/" element={<HomePage />} />
                  <Route path="/login" element={<LoginPage />} />
                  <Route path="/auth/callback" element={<CallbackPage />} />
                  
                  {/* Protected routes */}
                  <Route 
                    path="/characters" 
                    element={
                      <ProtectedRoute>
                        <CharacterDashboard />
                      </ProtectedRoute>
                    } 
                  />
                  
                  {/* Public utility routes */}
                  <Route path="/explore" element={<ExplorationPage />} />
                  <Route path="/manifest-explorer" element={<ManifestExplorer />} />
                  
                  {/* Catch all route */}
                  <Route path="*" element={<HomePage />} />
                </Routes>
              </Layout>
              
              {/* Global toast notifications */}
              <Toaster 
                position="top-right"
                toastOptions={{
                  duration: 4000,
                  className: 'toast-notification',
                }}
              />
            </div>
          </Router>
        </AuthProvider>
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;