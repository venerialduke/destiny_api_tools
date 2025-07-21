import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { apiClient } from '../services/apiClient';
import TableBrowser from '../components/explorer/TableBrowser';
import EntryList from '../components/explorer/EntryList';
import EntryExplorer from '../components/explorer/EntryExplorer';
import NavigationBreadcrumb from '../components/explorer/NavigationBreadcrumb';
import HashResolver from '../components/explorer/HashResolver';
import './ManifestExplorer.css';

const ManifestExplorer = () => {
    const navigate = useNavigate();
    
    // Navigation state
    const [currentView, setCurrentView] = useState('tables'); // 'tables', 'entries', 'entry'
    const [navigationPath, setNavigationPath] = useState([
        { type: 'home', label: 'Manifest Explorer', action: () => setCurrentView('tables') }
    ]);
    
    // Data state
    const [tables, setTables] = useState({});
    const [selectedTable, setSelectedTable] = useState(null);
    const [selectedEntry, setSelectedEntry] = useState(null);
    const [entryData, setEntryData] = useState(null);
    
    // UI state
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [hashResolver, setHashResolver] = useState({ show: false, hash: null });

    // Load tables on component mount
    useEffect(() => {
        loadTables();
    }, []);

    const loadTables = async () => {
        setLoading(true);
        setError(null);
        try {
            console.log('Loading manifest tables from API...');
            const response = await apiClient.get('/manifest/explorer/tables');
            console.log('Received tables response:', response);
            setTables(response);
        } catch (err) {
            console.error('Error loading tables:', err);
            if (err.message.includes('Network error')) {
                setError('Cannot connect to backend server. Please ensure the Flask server is running on http://localhost:5000');
            } else {
                setError(`Failed to load manifest tables: ${err.message}`);
            }
        } finally {
            setLoading(false);
        }
    };

    const navigateToTable = (tableName) => {
        setSelectedTable(tableName);
        setSelectedEntry(null);
        setEntryData(null);
        setCurrentView('entries');
        setNavigationPath([
            { type: 'home', label: 'Manifest Explorer', action: () => setCurrentView('tables') },
            { type: 'table', label: tableName, action: () => setCurrentView('entries') }
        ]);
    };

    const navigateToEntry = async (tableName, entryHash, entryName) => {
        setLoading(true);
        try {
            const response = await apiClient.get(`/manifest/explorer/entry/${tableName}/${entryHash}`);
            setSelectedEntry({ table: tableName, hash: entryHash, name: entryName });
            setEntryData(response);
            setCurrentView('entry');
            setNavigationPath(prev => [
                ...prev.slice(0, 2), // Keep home and table
                { 
                    type: 'entry', 
                    label: entryName || `Hash: ${entryHash}`,
                    action: () => setCurrentView('entry')
                }
            ]);
        } catch (err) {
            setError(`Failed to load entry ${entryHash}`);
            console.error('Error loading entry:', err);
        } finally {
            setLoading(false);
        }
    };

    const handleHashClick = (hash) => {
        setHashResolver({ show: true, hash });
    };

    const handleHashResolve = (tableName, entryHash, entryName) => {
        setHashResolver({ show: false, hash: null });
        navigateToEntry(tableName, entryHash, entryName);
    };

    const goBack = () => {
        if (currentView === 'entry') {
            setCurrentView('entries');
            setNavigationPath(prev => prev.slice(0, -1));
        } else if (currentView === 'entries') {
            setCurrentView('tables');
            setNavigationPath([
                { type: 'home', label: 'Manifest Explorer', action: () => setCurrentView('tables') }
            ]);
        }
    };

    return (
        <div className="manifest-explorer">
            <div className="explorer-header">
                <h1>Manifest Explorer</h1>
                <p>Explore all Destiny 2 manifest entries and discover relationships</p>
                
                <NavigationBreadcrumb 
                    path={navigationPath}
                    onNavigate={(pathItem) => pathItem.action()}
                />
            </div>

            {error && (
                <div className="error-message">
                    <div className="error-content">
                        <strong>Connection Error</strong>
                        <p>{error}</p>
                        <div className="error-actions">
                            <button onClick={loadTables} className="retry-btn">
                                Retry Connection
                            </button>
                            <button onClick={() => setError(null)} className="close-btn">
                                ×
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {loading && (
                <div className="loading-overlay">
                    <div className="loading-spinner">Loading...</div>
                </div>
            )}

            <div className="explorer-content">
                {currentView === 'tables' && (
                    <TableBrowser 
                        tables={tables}
                        onTableSelect={navigateToTable}
                        loading={loading}
                    />
                )}

                {currentView === 'entries' && selectedTable && (
                    <EntryList
                        tableName={selectedTable}
                        onEntrySelect={navigateToEntry}
                        onBack={goBack}
                    />
                )}

                {currentView === 'entry' && selectedEntry && entryData && (
                    <EntryExplorer
                        entryData={entryData}
                        onHashClick={handleHashClick}
                        onBack={goBack}
                    />
                )}
            </div>

            {hashResolver.show && (
                <HashResolver
                    hash={hashResolver.hash}
                    onResolve={handleHashResolve}
                    onClose={() => setHashResolver({ show: false, hash: null })}
                />
            )}
        </div>
    );
};

export default ManifestExplorer;