import React, { useState } from 'react';
import JSONTree from './JSONTree';
import './EntryExplorer.css';

const EntryExplorer = ({ entryData, onHashClick, onBack }) => {
    const [activeTab, setActiveTab] = useState('raw'); // 'raw', 'flattened', 'connections'
    const [expandedPaths, setExpandedPaths] = useState(new Set(['root']));

    if (!entryData) {
        return <div className="entry-explorer loading">Loading entry details...</div>;
    }

    const formatTableName = (name) => {
        return name.replace(/^Destiny/, '').replace(/Definition$/, '').replace(/([A-Z])/g, ' $1').trim();
    };

    const toggleExpand = (path) => {
        const newExpanded = new Set(expandedPaths);
        if (newExpanded.has(path)) {
            newExpanded.delete(path);
        } else {
            newExpanded.add(path);
        }
        setExpandedPaths(newExpanded);
    };

    const expandAll = () => {
        if (entryData.raw_data) {
            const allPaths = new Set(['root']);
            const findAllPaths = (obj, currentPath = 'root') => {
                if (typeof obj === 'object' && obj !== null) {
                    Object.keys(obj).forEach(key => {
                        const path = `${currentPath}.${key}`;
                        allPaths.add(path);
                        findAllPaths(obj[key], path);
                    });
                }
            };
            findAllPaths(entryData.raw_data);
            setExpandedPaths(allPaths);
        }
    };

    const collapseAll = () => {
        setExpandedPaths(new Set(['root']));
    };

    const renderHashReferences = () => {
        if (!entryData.hash_references || entryData.hash_references.length === 0) {
            return <p className="no-refs">No hash references found in this entry.</p>;
        }

        return (
            <div className="hash-references">
                <h4>Hash References Found ({entryData.hash_references.length})</h4>
                <div className="references-list">
                    {entryData.hash_references.map((ref, index) => (
                        <div key={index} className="reference-item">
                            <div className="reference-path">
                                <span className="path-text">{ref.path}</span>
                                <span className={`ref-type ${ref.type}`}>{ref.type}</span>
                            </div>
                            <button
                                className="hash-link"
                                onClick={() => onHashClick(ref.hash)}
                                title={`Explore hash ${ref.hash}`}
                            >
                                #{ref.hash}
                            </button>
                        </div>
                    ))}
                </div>
            </div>
        );
    };

    const renderFlattenedView = () => {
        if (!entryData.flattened_view || entryData.flattened_view.length === 0) {
            return <p className="no-data">No flattened data available.</p>;
        }

        const groupedData = {};
        entryData.flattened_view.forEach(item => {
            const category = item.path.split('.')[0];
            if (!groupedData[category]) {
                groupedData[category] = [];
            }
            groupedData[category].push(item);
        });

        return (
            <div className="flattened-view">
                {Object.entries(groupedData).map(([category, items]) => (
                    <div key={category} className="category-group">
                        <h4 className="category-title">{category}</h4>
                        <div className="category-items">
                            {items.map((item, index) => (
                                <div key={index} className="flattened-item">
                                    <span className="item-path">{item.path}</span>
                                    <span className={`item-type ${item.data_type.toLowerCase()}`}>
                                        {item.data_type}
                                    </span>
                                    {item.is_hash ? (
                                        <button
                                            className="hash-value clickable"
                                            onClick={() => onHashClick(item.value)}
                                            title={`Explore hash ${item.value}`}
                                        >
                                            {item.value}
                                        </button>
                                    ) : (
                                        <span className="item-value">
                                            {typeof item.value === 'string' && item.value.length > 100
                                                ? `${item.value.substring(0, 100)}...`
                                                : String(item.value)
                                            }
                                        </span>
                                    )}
                                </div>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
        );
    };

    return (
        <div className="entry-explorer">
            <div className="explorer-header">
                <div className="header-top">
                    <button onClick={onBack} className="back-btn">
                        ← Back to {formatTableName(entryData.table)}
                    </button>
                    <div className="entry-info">
                        <h2>{entryData.display_name}</h2>
                        <div className="entry-meta">
                            <span className="entry-hash">#{entryData.hash}</span>
                            <span className="entry-table">{entryData.table}</span>
                        </div>
                    </div>
                </div>

                {entryData.description && (
                    <div className="entry-description">
                        <p>{entryData.description}</p>
                    </div>
                )}
            </div>

            <div className="explorer-tabs">
                <button
                    className={`tab-btn ${activeTab === 'raw' ? 'active' : ''}`}
                    onClick={() => setActiveTab('raw')}
                >
                    Raw Data
                </button>
                <button
                    className={`tab-btn ${activeTab === 'flattened' ? 'active' : ''}`}
                    onClick={() => setActiveTab('flattened')}
                >
                    Flattened View
                </button>
                <button
                    className={`tab-btn ${activeTab === 'references' ? 'active' : ''}`}
                    onClick={() => setActiveTab('references')}
                >
                    Hash References ({entryData.hash_references?.length || 0})
                </button>
            </div>

            <div className="explorer-content">
                {activeTab === 'raw' && (
                    <div className="raw-data-view">
                        <div className="view-controls">
                            <button onClick={expandAll} className="control-btn">
                                Expand All
                            </button>
                            <button onClick={collapseAll} className="control-btn">
                                Collapse All
                            </button>
                        </div>
                        
                        {entryData.raw_data ? (
                            <JSONTree
                                data={entryData.raw_data}
                                expandedPaths={expandedPaths}
                                onToggleExpand={toggleExpand}
                                onHashClick={onHashClick}
                                path="root"
                            />
                        ) : (
                            <p className="no-data">No raw data available for this entry.</p>
                        )}
                    </div>
                )}

                {activeTab === 'flattened' && renderFlattenedView()}

                {activeTab === 'references' && renderHashReferences()}
            </div>
        </div>
    );
};

export default EntryExplorer;