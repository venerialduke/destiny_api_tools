import React, { useState, useEffect } from 'react';
import { setsService } from '../services/setsService';
import SetsTable from '../components/sets/SetsTable';
import SetsHeader from '../components/sets/SetsHeader';
import SetsFilter from '../components/sets/SetsFilter';
import LoadingSpinner from '../components/shared/LoadingSpinner';
import './EquipableSetsPage.css';

const EquipableSetsPage = () => {
    // State management
    const [sets, setSets] = useState([]);
    const [filteredSets, setFilteredSets] = useState([]);
    const [summary, setSummary] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    // Filter state
    const [selectedClass, setSelectedClass] = useState('all');
    const [searchTerm, setSearchTerm] = useState('');
    const [sortBy, setSortBy] = useState('name');

    // Load data on component mount
    useEffect(() => {
        loadSetsData();
    }, []);

    // Apply filters when sets or filter criteria change
    useEffect(() => {
        applyFilters();
    }, [sets, selectedClass, searchTerm, sortBy]);

    const loadSetsData = async () => {
        try {
            setLoading(true);
            setError(null);

            // Load sets and summary in parallel - include perks for table display
            const [setsResponse, summaryResponse] = await Promise.all([
                setsService.getAllSets({ includePerks: true }),
                setsService.getSummary()
            ]);

            // Load detailed data for each set to get perk information
            const setsWithDetails = await Promise.all(
                (setsResponse.data || []).map(async (set) => {
                    try {
                        const detailsResponse = await setsService.getSetDetails(set.hash);
                        return {
                            ...set,
                            setPerks: detailsResponse.data?.setPerks || []
                        };
                    } catch (error) {
                        console.error(`Error loading details for set ${set.hash}:`, error);
                        return { ...set, setPerks: [] };
                    }
                })
            );

            setSets(setsWithDetails);
            setSummary(summaryResponse.data || {});

        } catch (err) {
            console.error('Error loading sets data:', err);
            setError('Failed to load equipable sets. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    const applyFilters = () => {
        let filtered = [...sets];

        // Filter by class
        if (selectedClass !== 'all') {
            const classType = parseInt(selectedClass);
            filtered = filtered.filter(set => set.classType === classType);
        }

        // Filter by search term
        if (searchTerm.trim()) {
            const term = searchTerm.toLowerCase();
            filtered = filtered.filter(set => 
                set.name.toLowerCase().includes(term) ||
                set.description.toLowerCase().includes(term)
            );
        }

        // Sort sets
        filtered.sort((a, b) => {
            switch (sortBy) {
                case 'name':
                    return a.name.localeCompare(b.name);
                case 'pieces':
                    return b.totalPieces - a.totalPieces;
                case 'perks':
                    return b.perkCount - a.perkCount;
                case 'class':
                    return a.className.localeCompare(b.className);
                default:
                    return 0;
            }
        });

        setFilteredSets(filtered);
    };

    const handleClassFilter = (classType) => {
        setSelectedClass(classType);
    };

    const handleSearch = (term) => {
        setSearchTerm(term);
    };

    const handleSort = (sortOption) => {
        setSortBy(sortOption);
    };

    const handleRetry = () => {
        loadSetsData();
    };

    if (loading) {
        return (
            <div className="equipable-sets-page">
                <LoadingSpinner message="Loading equipable sets..." />
            </div>
        );
    }

    if (error) {
        return (
            <div className="equipable-sets-page">
                <div className="error-container">
                    <div className="error-content">
                        <h2>Error Loading Sets</h2>
                        <p>{error}</p>
                        <button onClick={handleRetry} className="retry-button">
                            Try Again
                        </button>
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className="equipable-sets-page">
            <SetsHeader 
                summary={summary}
                totalSets={sets.length}
                filteredCount={filteredSets.length}
            />

            <SetsFilter
                selectedClass={selectedClass}
                searchTerm={searchTerm}
                sortBy={sortBy}
                onClassFilter={handleClassFilter}
                onSearch={handleSearch}
                onSort={handleSort}
                summary={summary}
            />

            <div className="sets-content">
                {filteredSets.length > 0 ? (
                    <SetsTable sets={filteredSets} />
                ) : (
                    <div className="no-results">
                        <h3>No sets found</h3>
                        <p>Try adjusting your filters or search term.</p>
                    </div>
                )}
            </div>

            {filteredSets.length > 0 && (
                <div className="sets-footer">
                    <p>Showing {filteredSets.length} of {sets.length} equipable sets</p>
                </div>
            )}
        </div>
    );
};

export default EquipableSetsPage;