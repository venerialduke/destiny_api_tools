import React, { useState } from 'react';
import { setsService } from '../../services/setsService';
import DestinyImage from '../shared/DestinyImage';
import './SetCard.css';

const SetCard = ({ set }) => {
    const [expanded, setExpanded] = useState(false);
    const [detailsLoading, setDetailsLoading] = useState(false);
    const [detailedSet, setDetailedSet] = useState(null);
    const [error, setError] = useState(null);

    const handleToggleExpand = async () => {
        if (!expanded && !detailedSet) {
            // Load detailed data when expanding for the first time
            setDetailsLoading(true);
            setError(null);
            
            try {
                const response = await setsService.getSetDetails(set.hash);
                setDetailedSet(response.data);
            } catch (err) {
                console.error('Error loading set details:', err);
                setError('Failed to load set details');
            } finally {
                setDetailsLoading(false);
            }
        }
        
        setExpanded(!expanded);
    };

    const formatPerkRequirement = (count) => {
        if (count === 1) return '1 piece';
        return `${count} pieces`;
    };

    const getClassColor = (classType) => {
        return setsService.getClassColor(classType);
    };

    const groupArmorByType = (armorPieces) => {
        if (!armorPieces) return {};
        
        const groups = {};
        armorPieces.forEach(piece => {
            const type = piece.itemSubType || 'Unknown';
            if (!groups[type]) {
                groups[type] = [];
            }
            groups[type].push(piece);
        });
        
        return groups;
    };

    const displaySet = detailedSet || set;
    const hasDetailedData = !!detailedSet;

    return (
        <div className="set-card" style={{ '--class-color': getClassColor(set.classType) }}>
            <div className="set-card-header" onClick={handleToggleExpand}>
                <div className="set-icon-container">
                    <DestinyImage 
                        iconPath={set.icon}
                        alt={`${set.name} icon`}
                        useCase="card"
                        className="set-icon"
                    />
                </div>
                
                <div className="set-basic-info">
                    <div className="set-title-row">
                        <h3 className="set-name">{set.name}</h3>
                        <div className="set-class-badge">
                            {set.className}
                        </div>
                    </div>
                    
                    {set.description && (
                        <p className="set-description">{set.description}</p>
                    )}
                    
                    <div className="set-stats">
                        <div className="stat-item">
                            <span className="stat-icon">⚔️</span>
                            <span className="stat-label">Pieces:</span>
                            <span className="stat-value">{set.totalPieces}</span>
                        </div>
                        <div className="stat-item">
                            <span className="stat-icon">✨</span>
                            <span className="stat-label">Perks:</span>
                            <span className="stat-value">{set.perkCount}</span>
                        </div>
                        <div className="stat-item">
                            <span className="stat-icon">🔗</span>
                            <span className="stat-label">Hash:</span>
                            <span className="stat-value">{set.hash}</span>
                        </div>
                    </div>
                </div>
                
                <div className="expand-button">
                    <span className={`expand-icon ${expanded ? 'expanded' : ''}`}>
                        {expanded ? '▲' : '▼'}
                    </span>
                </div>
            </div>

            {expanded && (
                <div className="set-card-details">
                    {detailsLoading && (
                        <div className="details-loading">
                            <div className="loading-spinner-small"></div>
                            <span>Loading set details...</span>
                        </div>
                    )}

                    {error && (
                        <div className="details-error">
                            <span>⚠️ {error}</span>
                        </div>
                    )}

                    {hasDetailedData && (
                        <>
                            {/* Set Perks Section */}
                            {displaySet.setPerks && displaySet.setPerks.length > 0 && (
                                <div className="details-section">
                                    <h4 className="section-title">
                                        <span className="section-icon">✨</span>
                                        Set Perks
                                    </h4>
                                    <div className="perks-list">
                                        {displaySet.setPerks.map((perk, index) => (
                                            <div key={index} className="perk-item">
                                                <div className="perk-content">
                                                    <div className="perk-icon-container">
                                                        <DestinyImage 
                                                            iconPath={perk.icon}
                                                            alt={`${perk.name} icon`}
                                                            useCase="perk"
                                                            className="perk-icon"
                                                        />
                                                    </div>
                                                    <div className="perk-info">
                                                        <div className="perk-header">
                                                            <div className="perk-name">{perk.name}</div>
                                                            <div className="perk-requirement">
                                                                {formatPerkRequirement(perk.requiredCount)}
                                                            </div>
                                                        </div>
                                                        {perk.description && (
                                                            <div className="perk-description">
                                                                {perk.description}
                                                            </div>
                                                        )}
                                                    </div>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}

                            {/* Armor Pieces Section */}
                            {displaySet.armorPieces && displaySet.armorPieces.length > 0 && (
                                <div className="details-section">
                                    <h4 className="section-title">
                                        <span className="section-icon">⚔️</span>
                                        Armor Pieces ({displaySet.armorPieces.length})
                                    </h4>
                                    <div className="armor-groups">
                                        {Object.entries(groupArmorByType(displaySet.armorPieces)).map(([type, pieces]) => (
                                            <div key={type} className="armor-group">
                                                <div className="armor-type-header">
                                                    <span className="armor-type-name">
                                                        {setsService.formatArmorType(type)}
                                                    </span>
                                                    <span className="armor-type-count">
                                                        {pieces.length}
                                                    </span>
                                                </div>
                                                <div className="armor-pieces">
                                                    {pieces.slice(0, 3).map((piece, index) => (
                                                        <div key={piece.hash} className="armor-piece">
                                                            <div className="armor-piece-content">
                                                                <div className="armor-icon-container">
                                                                    <DestinyImage 
                                                                        iconPath={piece.icon}
                                                                        alt={`${piece.name} icon`}
                                                                        useCase="armor"
                                                                        className="armor-icon"
                                                                    />
                                                                </div>
                                                                <div className="piece-info">
                                                                    <div className="piece-name">{piece.name}</div>
                                                                    {pieces.length > 3 && index === 2 && (
                                                                        <div className="more-pieces">
                                                                            +{pieces.length - 3} more
                                                                        </div>
                                                                    )}
                                                                </div>
                                                            </div>
                                                        </div>
                                                    ))}
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}
                        </>
                    )}
                </div>
            )}
        </div>
    );
};

export default SetCard;