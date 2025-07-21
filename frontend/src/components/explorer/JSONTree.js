import React from 'react';
import './JSONTree.css';

const JSONTree = ({ data, expandedPaths, onToggleExpand, onHashClick, path = 'root' }) => {
    
    const isExpanded = (currentPath) => expandedPaths.has(currentPath);
    
    const isHashField = (key, value) => {
        if (typeof value !== 'number' || value <= 0) return false;
        const keyLower = key.toLowerCase();
        return keyLower.includes('hash') || keyLower.includes('definitionhash');
    };
    
    const isHashArrayField = (key, value) => {
        if (!Array.isArray(value)) return false;
        const keyLower = key.toLowerCase();
        
        // Standard hash array patterns
        if (keyLower.endsWith('hashes') || keyLower.includes('hash')) {
            return true;
        }
        
        // Known fields that contain hash arrays but don't have "hash" in the name
        // This should match the backend logic
        const knownHashArrays = [
            'setitems',          // DestinyEquipableItemSetDefinition
            'items',             // Various contexts where items are referenced
            'requirements',      // Some requirement lists contain hashes
            'rewards',           // Reward lists often contain item hashes
            'entries',           // Collection/presentation entries
            'children'           // Presentation node children
        ];
        
        // Check if this is a known hash array field with list of integers > 0
        if (knownHashArrays.includes(keyLower) && value.length > 0) {
            // Additional validation: check if list contains positive integers
            return value.slice(0, 5).every(item => typeof item === 'number' && item > 0);
        }
        
        return false;
    };

    const renderValue = (value, key, currentPath) => {
        // Null or undefined
        if (value === null) {
            return <span className="json-null">null</span>;
        }
        if (value === undefined) {
            return <span className="json-undefined">undefined</span>;
        }

        // Boolean
        if (typeof value === 'boolean') {
            return <span className="json-boolean">{value.toString()}</span>;
        }

        // Number
        if (typeof value === 'number') {
            if (isHashField(key, value)) {
                return (
                    <button
                        className="json-hash-link"
                        onClick={() => onHashClick(value)}
                        title={`Explore hash ${value}`}
                    >
                        {value}
                    </button>
                );
            }
            return <span className="json-number">{value}</span>;
        }

        // String
        if (typeof value === 'string') {
            const displayValue = value.length > 200 ? `${value.substring(0, 200)}...` : value;
            return <span className="json-string">"{displayValue}"</span>;
        }

        // Array
        if (Array.isArray(value)) {
            if (value.length === 0) {
                return <span className="json-empty-array">[]</span>;
            }

            const expanded = isExpanded(currentPath);
            
            return (
                <div className="json-array">
                    <button
                        className="json-toggle"
                        onClick={() => onToggleExpand(currentPath)}
                    >
                        {expanded ? '▼' : '▶'} [{value.length} items]
                    </button>
                    
                    {expanded && (
                        <div className="json-array-content">
                            {value.map((item, index) => {
                                const itemPath = `${currentPath}[${index}]`;
                                return (
                                    <div key={index} className="json-array-item">
                                        <span className="json-array-index">[{index}]:</span>
                                        <div className="json-array-value">
                                            {isHashArrayField(key, value) && typeof item === 'number' ? (
                                                <button
                                                    className="json-hash-link"
                                                    onClick={() => onHashClick(item)}
                                                    title={`Explore hash ${item}`}
                                                >
                                                    {item}
                                                </button>
                                            ) : (
                                                renderValue(item, `${key}[${index}]`, itemPath)
                                            )}
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    )}
                </div>
            );
        }

        // Object
        if (typeof value === 'object') {
            const keys = Object.keys(value);
            if (keys.length === 0) {
                return <span className="json-empty-object">{'{}'}</span>;
            }

            const expanded = isExpanded(currentPath);
            
            return (
                <div className="json-object">
                    <button
                        className="json-toggle"
                        onClick={() => onToggleExpand(currentPath)}
                    >
                        {expanded ? '▼' : '▶'} {'{'}...{'}'}  ({keys.length} properties)
                    </button>
                    
                    {expanded && (
                        <div className="json-object-content">
                            {keys.map((objKey) => {
                                const objPath = `${currentPath}.${objKey}`;
                                return (
                                    <div key={objKey} className="json-property">
                                        <span className="json-property-key">"{objKey}":</span>
                                        <div className="json-property-value">
                                            {renderValue(value[objKey], objKey, objPath)}
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    )}
                </div>
            );
        }

        return <span className="json-unknown">{String(value)}</span>;
    };

    return (
        <div className="json-tree">
            <div className="json-root">
                {renderValue(data, 'root', path)}
            </div>
        </div>
    );
};

export default JSONTree;