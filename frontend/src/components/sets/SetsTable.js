import React from 'react';
import DestinyImage from '../shared/DestinyImage';
import './SetsTable.css';

const SetsTable = ({ sets }) => {
    const getClassColor = (classType) => {
        const classColors = {
            0: '#f24c3d', // Titan - Red
            1: '#4a90e2', // Hunter - Blue
            2: '#f39c12', // Warlock - Orange
            3: '#95a5a6'  // Unknown - Gray
        };
        return classColors[classType] || '#95a5a6';
    };

    const getPerkByRequiredCount = (setPerks, requiredCount) => {
        return setPerks.find(perk => perk.requiredCount === requiredCount);
    };

    if (!sets || sets.length === 0) {
        return (
            <div className="sets-table-empty">
                <p>No equipable sets found.</p>
            </div>
        );
    }

    return (
        <div className="sets-table-container">
            <div className="sets-table">
                <div className="table-header">
                    <div className="header-cell set-name-header">Set</div>
                    <div className="header-cell perk-header">2-Piece Bonus</div>
                    <div className="header-cell perk-header">4-Piece Bonus</div>
                </div>

                <div className="table-body">
                    {sets.map((set) => {
                        const twoPiecePerk = getPerkByRequiredCount(set.setPerks || [], 2);
                        const fourPiecePerk = getPerkByRequiredCount(set.setPerks || [], 4);

                        return (
                            <div 
                                key={set.hash} 
                                className="table-row"
                                style={{ '--class-color': getClassColor(set.classType) }}
                            >
                                {/* Set Information Column */}
                                <div className="table-cell set-info-cell">
                                    <div className="set-info">
                                        <div className="set-icon-wrapper">
                                            <DestinyImage 
                                                iconPath={set.icon}
                                                alt={`${set.name} icon`}
                                                useCase="card"
                                                className="set-table-icon"
                                            />
                                        </div>
                                        <div className="set-details">
                                            <div className="set-name">{set.name}</div>
                                            {set.description && (
                                                <div className="set-description">
                                                    {set.description}
                                                </div>
                                            )}
                                        </div>
                                    </div>
                                </div>

                                {/* 2-Piece Perk Column */}
                                <div className="table-cell perk-cell" data-label="2-Piece Bonus">
                                    {twoPiecePerk ? (
                                        <div className="perk-info">
                                            <div className="perk-icon-wrapper">
                                                <DestinyImage 
                                                    iconPath={twoPiecePerk.icon}
                                                    alt={`${twoPiecePerk.name} icon`}
                                                    useCase="perk"
                                                    className="perk-table-icon"
                                                />
                                            </div>
                                            <div className="perk-details">
                                                <div className="perk-name">{twoPiecePerk.name}</div>
                                                {twoPiecePerk.description && (
                                                    <div className="perk-description">
                                                        {twoPiecePerk.description}
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    ) : (
                                        <div className="no-perk">No 2-piece bonus</div>
                                    )}
                                </div>

                                {/* 4-Piece Perk Column */}
                                <div className="table-cell perk-cell" data-label="4-Piece Bonus">
                                    {fourPiecePerk ? (
                                        <div className="perk-info">
                                            <div className="perk-icon-wrapper">
                                                <DestinyImage 
                                                    iconPath={fourPiecePerk.icon}
                                                    alt={`${fourPiecePerk.name} icon`}
                                                    useCase="perk"
                                                    className="perk-table-icon"
                                                />
                                            </div>
                                            <div className="perk-details">
                                                <div className="perk-name">{fourPiecePerk.name}</div>
                                                {fourPiecePerk.description && (
                                                    <div className="perk-description">
                                                        {fourPiecePerk.description}
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    ) : (
                                        <div className="no-perk">No 4-piece bonus</div>
                                    )}
                                </div>
                            </div>
                        );
                    })}
                </div>
            </div>
        </div>
    );
};

export default SetsTable;