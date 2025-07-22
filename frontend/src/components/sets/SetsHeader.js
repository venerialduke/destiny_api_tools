import React from 'react';
import './SetsHeader.css';

const SetsHeader = ({ summary, totalSets, filteredCount }) => {
    const getClassIcon = (className) => {
        const icons = {
            'Titan': '🛡️',
            'Hunter': '🏹', 
            'Warlock': '🔮'
        };
        return icons[className] || '❓';
    };

    return (
        <div className="sets-header">
            <div className="header-content">
                <div className="title-section">
                    <h1>Equipable Item Sets</h1>
                    <p className="subtitle">
                        Discover complete armor sets with powerful set bonuses and unique perks
                    </p>
                </div>

                {summary && (
                    <div className="summary-stats">
                        <div className="stat-grid">
                            <div className="stat-card total">
                                <div className="stat-value">{summary.total_sets || 0}</div>
                                <div className="stat-label">Total Sets</div>
                            </div>

                            <div className="stat-card perks">
                                <div className="stat-value">{summary.total_perks || 0}</div>
                                <div className="stat-label">Set Perks</div>
                            </div>

                            <div className="stat-card avg">
                                <div className="stat-value">
                                    {summary.average_perks_per_set ? 
                                        summary.average_perks_per_set.toFixed(1) : '0'
                                    }
                                </div>
                                <div className="stat-label">Avg Perks</div>
                            </div>
                        </div>

                        {summary.sets_by_class && (
                            <div className="class-breakdown">
                                <h3>Sets by Class</h3>
                                <div className="class-stats">
                                    {Object.entries(summary.sets_by_class).map(([className, count]) => (
                                        <div key={className} className="class-stat">
                                            <span className="class-icon">{getClassIcon(className)}</span>
                                            <span className="class-name">{className}</span>
                                            <span className="class-count">{count}</span>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}
                    </div>
                )}

                {filteredCount !== totalSets && (
                    <div className="filter-summary">
                        <span className="filter-text">
                            Showing {filteredCount} of {totalSets} sets
                        </span>
                    </div>
                )}
            </div>
        </div>
    );
};

export default SetsHeader;