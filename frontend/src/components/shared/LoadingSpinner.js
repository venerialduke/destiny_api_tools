import React from 'react';
import './LoadingSpinner.css';

const LoadingSpinner = ({ message = 'Loading...', size = 'medium' }) => {
    return (
        <div className="loading-container">
            <div className={`loading-spinner ${size}`}>
                <div className="spinner-ring"></div>
                <div className="spinner-ring"></div>
                <div className="spinner-ring"></div>
                <div className="spinner-ring"></div>
            </div>
            {message && (
                <div className="loading-message">{message}</div>
            )}
        </div>
    );
};

export default LoadingSpinner;