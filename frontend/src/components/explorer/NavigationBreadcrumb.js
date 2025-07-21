import React from 'react';
import './NavigationBreadcrumb.css';

const NavigationBreadcrumb = ({ path, onNavigate }) => {
    if (!path || path.length === 0) {
        return null;
    }

    return (
        <nav className="navigation-breadcrumb">
            <div className="breadcrumb-container">
                {path.map((pathItem, index) => (
                    <div key={index} className="breadcrumb-item">
                        {index > 0 && <span className="breadcrumb-separator">→</span>}
                        <button
                            className={`breadcrumb-link ${index === path.length - 1 ? 'current' : ''}`}
                            onClick={() => onNavigate(pathItem)}
                            disabled={index === path.length - 1}
                        >
                            {pathItem.label}
                        </button>
                    </div>
                ))}
            </div>
        </nav>
    );
};

export default NavigationBreadcrumb;