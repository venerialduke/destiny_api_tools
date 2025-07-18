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

// Tool pages
import InventoryManagerPage from './pages/tools/InventoryManagerPage';
import LoadoutManagerPage from './pages/tools/LoadoutManagerPage';
import StatsTrackerPage from './pages/tools/StatsTrackerPage';
import FireteamFinderPage from './pages/tools/FireteamFinderPage';
import VendorTrackerPage from './pages/tools/VendorTrackerPage';

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
                  
                  {/* Protected tool routes */}
                  <Route 
                    path="/tools/inventory" 
                    element={
                      <ProtectedRoute>
                        <InventoryManagerPage />
                      </ProtectedRoute>
                    } 
                  />
                  <Route 
                    path="/tools/loadouts" 
                    element={
                      <ProtectedRoute>
                        <LoadoutManagerPage />
                      </ProtectedRoute>
                    } 
                  />
                  <Route 
                    path="/tools/stats" 
                    element={
                      <ProtectedRoute>
                        <StatsTrackerPage />
                      </ProtectedRoute>
                    } 
                  />
                  <Route 
                    path="/tools/fireteam" 
                    element={
                      <ProtectedRoute>
                        <FireteamFinderPage />
                      </ProtectedRoute>
                    } 
                  />
                  <Route 
                    path="/tools/vendors" 
                    element={
                      <ProtectedRoute>
                        <VendorTrackerPage />
                      </ProtectedRoute>
                    } 
                  />
                  
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