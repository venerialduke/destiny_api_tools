import React from 'react';
import './SetsFilter.css';

const SetsFilter = ({ 
    selectedClass, 
    searchTerm, 
    sortBy, 
    onClassFilter, 
    onSearch, 
    onSort, 
    summary 
}) => {
    const classOptions = [
        { value: 'all', label: 'All Classes', icon: '⚔️' },
        { value: '0', label: 'Titan', icon: '🛡️' },
        { value: '1', label: 'Hunter', icon: '🏹' },
        { value: '2', label: 'Warlock', icon: '🔮' }
    ];

    const sortOptions = [
        { value: 'name', label: 'Name' },
        { value: 'pieces', label: 'Armor Pieces' },
        { value: 'perks', label: 'Set Perks' },
        { value: 'class', label: 'Class' }
    ];

    const getClassCount = (classValue) => {
        if (!summary || !summary.sets_by_class) return 0;
        
        if (classValue === 'all') {
            return summary.total_sets || 0;
        }
        
        const className = classOptions.find(opt => opt.value === classValue)?.label;
        return summary.sets_by_class[className] || 0;
    };

    return (
        <div className="sets-filter">
            <div className="filter-section">
                <div className="filter-group">
                    <label className="filter-label">Class Filter</label>
                    <div className="class-buttons">
                        {classOptions.map(option => (
                            <button
                                key={option.value}
                                className={`class-button ${selectedClass === option.value ? 'active' : ''}`}
                                onClick={() => onClassFilter(option.value)}
                                title={`${option.label} (${getClassCount(option.value)} sets)`}
                            >
                                <span className="class-icon">{option.icon}</span>
                                <span className="class-label">{option.label}</span>
                                <span className="class-count">{getClassCount(option.value)}</span>
                            </button>
                        ))}
                    </div>
                </div>

                <div className="filter-group">
                    <label className="filter-label" htmlFor="search-input">Search Sets</label>
                    <div className="search-container">
                        <input
                            id="search-input"
                            type="text"
                            placeholder="Search by name or description..."
                            value={searchTerm}
                            onChange={(e) => onSearch(e.target.value)}
                            className="search-input"
                        />
                        <div className="search-icon">🔍</div>
                    </div>
                </div>

                <div className="filter-group">
                    <label className="filter-label" htmlFor="sort-select">Sort By</label>
                    <select
                        id="sort-select"
                        value={sortBy}
                        onChange={(e) => onSort(e.target.value)}
                        className="sort-select"
                    >
                        {sortOptions.map(option => (
                            <option key={option.value} value={option.value}>
                                {option.label}
                            </option>
                        ))}
                    </select>
                </div>
            </div>
        </div>
    );
};

export default SetsFilter;