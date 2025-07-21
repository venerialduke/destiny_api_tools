import React, { useState, useEffect } from 'react';
import { apiClient } from '../../services/apiClient';
import './EntryList.css';

const EntryList = ({ tableName, onEntrySelect, onBack }) => {
    const [entries, setEntries] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const [pagination, setPagination] = useState({});
    const [totalEntries, setTotalEntries] = useState(0);
    
    const entriesPerPage = 50;

    useEffect(() => {
        loadEntries();
    }, [tableName, currentPage, searchTerm]);

    useEffect(() => {
        // Reset page when search changes
        if (currentPage !== 1) {
            setCurrentPage(1);
        } else {
            loadEntries();
        }
    }, [searchTerm]);

    const loadEntries = async () => {
        setLoading(true);
        setError(null);
        
        try {
            const response = await apiClient.get(`/manifest/explorer/table/${tableName}`, {
                params: {
                    page: currentPage,
                    limit: entriesPerPage,
                    search: searchTerm
                }
            });

            setEntries(response.entries);
            setPagination(response.pagination);
            setTotalEntries(response.pagination.total);
        } catch (err) {
            setError(`Failed to load entries from ${tableName}`);
            console.error('Error loading entries:', err);
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
        setSearchTerm(e.target.value);
        setCurrentPage(1); // Reset to first page when searching
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
                        value={searchTerm}
                        onChange={handleSearchChange}
                        className="search-input"
                    />
                </div>
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
                        {entries.map((entry, index) => (
                            <div
                                key={entry.hash}
                                className="entry-card"
                                onClick={() => handleEntryClick(entry)}
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
                    </div>

                    {entries.length === 0 && !loading && (
                        <div className="no-entries">
                            <p>No entries found{searchTerm && ` matching "${searchTerm}"`}.</p>
                            {searchTerm && (
                                <button onClick={() => setSearchTerm('')} className="clear-search-btn">
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