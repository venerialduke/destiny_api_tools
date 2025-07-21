import React, { useState } from 'react';
import './TableBrowser.css';

const TableBrowser = ({ tables, onTableSelect, loading }) => {
    const [searchTerm, setSearchTerm] = useState('');
    const [selectedCategory, setSelectedCategory] = useState('All');

    if (loading || !tables || !tables.tables) {
        return (
            <div className="table-browser loading">
                <div className="loading-content">
                    <div className="loading-spinner"></div>
                    <h3>Loading Manifest Tables</h3>
                    <p>Connecting to database and analyzing {tables?.total_tables || '97+'} definition tables...</p>
                    <div className="loading-details">
                        <p>This loads table metadata only - individual entries are loaded on-demand for optimal performance.</p>
                        {!tables && (
                            <p className="connection-status">
                                <span className="status-indicator">●</span> 
                                Connecting to backend server...
                            </p>
                        )}
                    </div>
                </div>
            </div>
        );
    }

    const { tables: tableList, categorized } = tables;
    const categories = ['All', ...Object.keys(categorized)];

    // Filter tables based on search and category
    const filteredTables = tableList.filter(table => {
        const matchesSearch = table.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                            table.sample_entry.toLowerCase().includes(searchTerm.toLowerCase());
        const matchesCategory = selectedCategory === 'All' || table.category === selectedCategory;
        return matchesSearch && matchesCategory;
    });

    const formatTableName = (name) => {
        // Convert "DestinyInventoryItemDefinition" to "Inventory Item Definition"
        return name.replace(/^Destiny/, '').replace(/Definition$/, '').replace(/([A-Z])/g, ' $1').trim();
    };

    return (
        <div className="table-browser">
            <div className="browser-controls">
                <div className="search-section">
                    <input
                        type="text"
                        placeholder="Search tables..."
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        className="search-input"
                    />
                </div>
                
                <div className="category-filter">
                    {categories.map(category => (
                        <button
                            key={category}
                            className={`category-btn ${selectedCategory === category ? 'active' : ''}`}
                            onClick={() => setSelectedCategory(category)}
                        >
                            {category} {category !== 'All' && `(${categorized[category]?.length || 0})`}
                        </button>
                    ))}
                </div>
            </div>

            <div className="tables-grid">
                {filteredTables.map(table => (
                    <div
                        key={table.name}
                        className="table-card"
                        onClick={() => onTableSelect(table.name)}
                    >
                        <div className="table-header">
                            <h3>{formatTableName(table.name)}</h3>
                            <span className="record-count">{table.record_count.toLocaleString()} entries</span>
                        </div>
                        <div className="table-meta">
                            <span className="category-tag">{table.category}</span>
                            <p className="sample-entry">Sample: {table.sample_entry}</p>
                        </div>
                        <div className="table-footer">
                            <span className="table-full-name">{table.name}</span>
                        </div>
                    </div>
                ))}
            </div>

            {filteredTables.length === 0 && (
                <div className="no-results">
                    <p>No tables found matching your criteria.</p>
                    <button onClick={() => { setSearchTerm(''); setSelectedCategory('All'); }}>
                        Clear Filters
                    </button>
                </div>
            )}

            <div className="browser-stats">
                <p>
                    Showing {filteredTables.length} of {tableList.length} tables
                    {selectedCategory !== 'All' && ` in category "${selectedCategory}"`}
                </p>
            </div>
        </div>
    );
};

export default TableBrowser;