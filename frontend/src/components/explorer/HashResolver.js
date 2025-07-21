import React, { useState, useEffect } from 'react';
import { apiClient } from '../../services/apiClient';
import './HashResolver.css';

const HashResolver = ({ hash, onResolve, onClose }) => {
    const [matches, setMatches] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (hash) {
            resolveHash();
        }
    }, [hash]);

    const resolveHash = async () => {
        setLoading(true);
        setError(null);
        
        try {
            const response = await apiClient.get(`/manifest/explorer/resolve/${hash}`);
            setMatches(response.matches);
        } catch (err) {
            setError(`Failed to resolve hash ${hash}`);
            console.error('Error resolving hash:', err);
        } finally {
            setLoading(false);
        }
    };

    const formatTableName = (name) => {
        return name.replace(/^Destiny/, '').replace(/Definition$/, '').replace(/([A-Z])/g, ' $1').trim();
    };

    const handleMatchClick = (match) => {
        onResolve(match.table, match.hash, match.display_name);
    };

    return (
        <div className="hash-resolver-overlay" onClick={onClose}>
            <div className="hash-resolver-modal" onClick={e => e.stopPropagation()}>
                <div className="resolver-header">
                    <h3>Hash Resolution: #{hash}</h3>
                    <button onClick={onClose} className="close-btn">×</button>
                </div>

                <div className="resolver-content">
                    {loading && (
                        <div className="resolver-loading">
                            <p>Searching for hash #{hash}...</p>
                        </div>
                    )}

                    {error && (
                        <div className="resolver-error">
                            <p>{error}</p>
                            <button onClick={resolveHash} className="retry-btn">
                                Try Again
                            </button>
                        </div>
                    )}

                    {!loading && !error && (
                        <>
                            {matches.length > 0 ? (
                                <div className="matches-container">
                                    <p className="matches-header">
                                        Found {matches.length} match{matches.length !== 1 ? 'es' : ''}:
                                    </p>
                                    <div className="matches-list">
                                        {matches.map((match, index) => (
                                            <div
                                                key={index}
                                                className="match-item"
                                                onClick={() => handleMatchClick(match)}
                                            >
                                                <div className="match-header">
                                                    <h4 className="match-name">
                                                        {match.display_name}
                                                    </h4>
                                                    <span className="match-table">
                                                        {formatTableName(match.table)}
                                                    </span>
                                                </div>
                                                
                                                {match.description && (
                                                    <p className="match-description">
                                                        {match.description}
                                                    </p>
                                                )}
                                                
                                                <div className="match-footer">
                                                    <span className="match-hash">#{match.hash}</span>
                                                    <span className="match-type">{match.match_type}</span>
                                                    <span className="click-hint">Click to explore →</span>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            ) : (
                                <div className="no-matches">
                                    <p>No entries found with hash #{hash}</p>
                                    <p className="no-matches-help">
                                        This hash might reference an entry that doesn't exist in the current manifest,
                                        or it could be a computed value.
                                    </p>
                                </div>
                            )}
                        </>
                    )}
                </div>

                <div className="resolver-footer">
                    <button onClick={onClose} className="cancel-btn">
                        Cancel
                    </button>
                    {matches.length > 0 && (
                        <button onClick={() => handleMatchClick(matches[0])} className="go-to-first-btn">
                            Go to First Match
                        </button>
                    )}
                </div>
            </div>
        </div>
    );
};

export default HashResolver;