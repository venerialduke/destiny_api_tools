import React, { useState, useEffect } from 'react';
import { apiClient } from '../../services/apiClient';
import './EntryList.css';

const EntryList = ({ tableName, onEntrySelect, onBack }) => {
    const [entries, setEntries] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [searchTerm, setSearchTerm] = useState('');
    const [searchInput, setSearchInput] = useState(''); // For immediate UI updates
    const [currentPage, setCurrentPage] = useState(1);
    const [pagination, setPagination] = useState({});
    const [totalEntries, setTotalEntries] = useState(0);
    const [apiCallCounter, setApiCallCounter] = useState(0);
    
    const entriesPerPage = 50;

    useEffect(() => {
        console.log('🔄 useEffect triggered - about to loadEntries');
        console.log('  tableName:', tableName);
        console.log('  currentPage:', currentPage);
        console.log('  searchTerm:', searchTerm);
        loadEntries();
    }, [tableName, currentPage, searchTerm]);

    // Debounced search effect
    useEffect(() => {
        const timeoutId = setTimeout(() => {
            console.log('⏱️ Search timeout triggered, updating searchTerm:', searchInput);
            console.log('  Previous searchTerm:', searchTerm);
            console.log('  New searchTerm will be:', searchInput);
            setSearchTerm(searchInput);
            if (currentPage !== 1) {
                console.log('  Resetting page to 1');
                setCurrentPage(1);
            }
        }, 500); // 500ms delay

        return () => {
            clearTimeout(timeoutId);
        };
    }, [searchInput]); // REMOVED currentPage dependency to prevent race conditions

    // Debug effect to track entries state changes
    useEffect(() => {
        console.log('🔄 Entries state changed:');
        console.log('  new entries length:', entries.length);
        console.log('  entries is array:', Array.isArray(entries));
        console.log('  first entry:', entries[0]);
    }, [entries]);

    const loadEntries = async () => {
        const callId = apiCallCounter + 1;
        setApiCallCounter(callId);
        
        console.log(`📋 [Call #${callId}] Loading entries for table:`);
        console.log('  tableName:', tableName);
        console.log('  currentPage:', currentPage);
        console.log('  searchTerm:', searchTerm);
        console.log('  entriesPerPage:', entriesPerPage);
        
        setLoading(true);
        setError(null);
        
        try {
            const requestParams = {
                page: currentPage,
                limit: entriesPerPage,
                search: searchTerm
            };
            
            console.log(`🌐 [Call #${callId}] Making API request with params:`);
            console.log('  page:', requestParams.page);
            console.log('  limit:', requestParams.limit);
            console.log('  search:', requestParams.search);
            
            // Use _makeRequest directly to bypass BaseService parameter issues
            const response = await apiClient._makeRequest('GET', `/manifest/explorer/table/${tableName}`, null, {
                params: requestParams
            });

            console.log(`✅ [Call #${callId}] API response received:`);
            console.log('  responseType:', typeof response);
            console.log('  responseKeys:', Object.keys(response || {}));
            console.log('  response.entries length:', response.entries?.length || 0);
            console.log('  response.pagination:', response.pagination);
            console.log('  response.search:', response.search);
            console.log('  first entry:', response.entries?.[0]);

            // Handle potential BaseService wrapping
            const responseData = response.data || response;
            const entries = responseData.entries || [];
            const pagination = responseData.pagination || {};
            
            console.log(`🔄 [Call #${callId}] Setting state with:`);
            console.log('  entries length:', entries.length);
            console.log('  entries array:', Array.isArray(entries));
            console.log('  entries sample:', entries.slice(0, 2));
            console.log('  pagination:', pagination);
            console.log('  totalEntries:', pagination.total || 0);
            
            setEntries(entries);
            setPagination(pagination);
            setTotalEntries(pagination.total || 0);
            
            // Add a small delay to check if state updates properly
            setTimeout(() => {
                console.log('⏰ State after update (delayed check):');
                console.log('  entries state length:', entries.length);
                console.log('  first entry after state set:', entries[0]);
            }, 100);
        } catch (err) {
            console.error('❌ Error loading entries:', {
                tableName,
                currentPage,
                searchTerm,
                error: err.message,
                status: err.response?.status,
                statusText: err.response?.statusText,
                data: err.response?.data
            });
            setError(`Failed to load entries from ${tableName}`);
        } finally {
            setLoading(false);
        }
    };

    const formatTableName = (name) => {
        return name.replace(/^Destiny/, '').replace(/Definition$/, '').replace(/([A-Z])/g, ' $1').trim();
    };

    const handleEntryClick = (entry) => {
        onEntrySelect(tableName, entry.hash, entry.display_name);
    };

    const handlePageChange = (newPage) => {
        setCurrentPage(newPage);
    };

    const handleSearchChange = (e) => {
        const value = e.target.value;
        console.log('🔍 Search input changed:');
        console.log('  value:', value);
        console.log('  previousSearchInput:', searchInput);
        console.log('  previousSearchTerm:', searchTerm);
        console.log('  currentPage:', currentPage);
        console.log('  tableName:', tableName);
        setSearchInput(value); // Update immediate UI state
        // The debounced effect will handle updating searchTerm
    };

    const renderPagination = () => {
        if (!pagination.total || pagination.total <= entriesPerPage) return null;

        const totalPages = Math.ceil(pagination.total / entriesPerPage);
        const pages = [];
        
        // Show first page
        if (currentPage > 3) {
            pages.push(1);
            if (currentPage > 4) pages.push('...');
        }
        
        // Show pages around current page
        for (let i = Math.max(1, currentPage - 2); i <= Math.min(totalPages, currentPage + 2); i++) {
            pages.push(i);
        }
        
        // Show last page
        if (currentPage < totalPages - 2) {
            if (currentPage < totalPages - 3) pages.push('...');
            pages.push(totalPages);
        }

        return (
            <div className="pagination">
                <button
                    onClick={() => handlePageChange(currentPage - 1)}
                    disabled={currentPage === 1}
                    className="pagination-btn"
                >
                    Previous
                </button>
                
                {pages.map((page, index) => (
                    <button
                        key={index}
                        onClick={() => typeof page === 'number' && handlePageChange(page)}
                        className={`pagination-btn ${page === currentPage ? 'active' : ''} ${typeof page !== 'number' ? 'disabled' : ''}`}
                        disabled={typeof page !== 'number'}
                    >
                        {page}
                    </button>
                ))}
                
                <button
                    onClick={() => handlePageChange(currentPage + 1)}
                    disabled={currentPage === totalPages}
                    className="pagination-btn"
                >
                    Next
                </button>
            </div>
        );
    };

    return (
        <div className="entry-list">
            <div className="entry-list-header">
                <div className="header-top">
                    <button onClick={onBack} className="back-btn">
                        ← Back to Tables
                    </button>
                    <h2>{formatTableName(tableName)}</h2>
                </div>
                
                <div className="header-meta">
                    <span className="entry-count">
                        {totalEntries.toLocaleString()} total entries
                    </span>
                    <span className="table-tech-name">{tableName}</span>
                </div>

                <div className="search-section">
                    <input
                        type="text"
                        placeholder="Search entries by name or description..."
                        value={searchInput}
                        onChange={handleSearchChange}
                        className="search-input"
                        style={{
                            color: '#2c3e50',
                            backgroundColor: '#ffffff',
                            caretColor: '#2c3e50'
                        }}
                    />
                </div>
            </div>

            {/* Debug info - always visible */}
            <div style={{
                background: '#f0f0f0', 
                padding: '10px', 
                margin: '10px 0', 
                border: '1px solid #ccc',
                fontSize: '12px',
                fontFamily: 'monospace'
            }}>
                <strong>Debug Info:</strong><br />
                Loading: {loading.toString()}<br />
                Error: {error || 'none'}<br />
                Entries Length: {entries.length}<br />
                Entries is Array: {Array.isArray(entries).toString()}<br />
                Total Entries: {totalEntries}<br />
                Search Term: "{searchTerm}"<br />
                Search Input: "{searchInput}"<br />
                First Entry Hash: {entries[0]?.hash || 'none'}<br />
                <button 
                    onClick={() => {
                        console.log('🧪 Manual search test - forcing searchTerm = "gjallarhorn"');
                        setSearchTerm('gjallarhorn');
                        setSearchInput('gjallarhorn');
                    }}
                    style={{background: 'red', color: 'white', padding: '5px'}}
                >
                    TEST: Force Search "gjallarhorn"
                </button>
                <br />
                <button 
                    onClick={async () => {
                        console.log('🧪 BLUE BUTTON CLICKED - Direct API test starting...');
                        console.log('  tableName:', tableName);
                        
                        try {
                            console.log('🧪 About to make direct API call...');
                            
                            // Try direct _makeRequest to bypass BaseService
                            console.log('🧪 Testing direct _makeRequest...');
                            const directResponse = await apiClient._makeRequest('GET', `/manifest/explorer/table/${tableName}`, null, {
                                params: { page: 1, limit: 5, search: 'gjallarhorn' }
                            });
                            console.log('🧪 Direct _makeRequest SUCCESS:', directResponse);
                            
                            alert('Direct API call completed - check console');
                        } catch (err) {
                            console.error('🧪 Direct API ERROR:', err);
                            alert('Direct API call failed - check console');
                        }
                    }}
                    style={{background: 'blue', color: 'white', padding: '5px'}}
                >
                    TEST: Direct API Call
                </button>
            </div>

            {error && (
                <div className="error-message">
                    {error}
                </div>
            )}

            {loading ? (
                <div className="loading-section">
                    <p>Loading entries...</p>
                </div>
            ) : (
                <>
                    <div className="entries-container">
                        {/* Simplified render logging */}
                        <div style={{background: 'lightblue', padding: '10px', margin: '10px'}}>
                            Test element - this should always be visible
                        </div>
                        
                        {Array.isArray(entries) && entries.length > 0 ? (
                            <div style={{background: 'lightgreen', padding: '10px', margin: '10px'}}>
                                About to render {entries.length} entries
                                {console.log('✅ Rendering', entries.length, 'entries')}
                            </div>
                        ) : (
                            <div style={{background: 'lightcoral', padding: '10px', margin: '10px'}}>
                                No entries to render - length: {entries.length}, isArray: {Array.isArray(entries).toString()}
                            </div>
                        )}
                        
                        {Array.isArray(entries) && entries.length > 0 && entries.map((entry, index) => (
                            <div
                                key={entry.hash}
                                className="entry-card"
                                onClick={() => handleEntryClick(entry)}
                                style={{
                                    border: '2px solid red',
                                    margin: '10px',
                                    padding: '10px',
                                    backgroundColor: 'yellow',
                                    minHeight: '100px'
                                }}
                            >
                                <div className="entry-header">
                                    <h3 className="entry-name">
                                        {entry.display_name || 'Unnamed Entry'}
                                    </h3>
                                    <span className="entry-hash">#{entry.hash}</span>
                                </div>
                                
                                {entry.description && (
                                    <p className="entry-description">
                                        {entry.description.length > 200 
                                            ? `${entry.description.substring(0, 200)}...` 
                                            : entry.description}
                                    </p>
                                )}
                                
                                <div className="entry-footer">
                                    <span className="entry-index">Entry {((currentPage - 1) * entriesPerPage) + index + 1}</span>
                                    <span className="click-hint">Click to explore →</span>
                                </div>
                            </div>
                        ))}
                        
                        <div style={{background: 'orange', padding: '10px', margin: '10px'}}>
                            Finished rendering entries section - {entries.length} entries
                        </div>
                    </div>

                    {entries.length === 0 && !loading && (
                        <div className="no-entries">
                            <p>No entries found{searchTerm && ` matching "${searchTerm}"`}.</p>
                            {searchTerm && (
                                <button onClick={() => {
                                    setSearchInput('');
                                    setSearchTerm('');
                                }} className="clear-search-btn">
                                    Clear Search
                                </button>
                            )}
                        </div>
                    )}

                    {renderPagination()}

                    <div className="list-stats">
                        <p>
                            Showing entries {((currentPage - 1) * entriesPerPage) + 1} - {Math.min(currentPage * entriesPerPage, totalEntries)} 
                            of {totalEntries.toLocaleString()}
                            {searchTerm && ` matching "${searchTerm}"`}
                        </p>
                    </div>
                </>
            )}
        </div>
    );
};

export default EntryList;