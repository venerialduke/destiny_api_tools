import React, { useState, useEffect } from 'react';
import { imageService } from '../../services/imageService';
import './DestinyImage.css';

const DestinyImage = ({ 
    iconPath, 
    alt = '', 
    className = '', 
    size = 'medium',
    format = 'webp',
    useCase = 'card',
    showPlaceholder = true,
    onLoad,
    onError,
    ...props 
}) => {
    const [imageUrl, setImageUrl] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);

    useEffect(() => {
        if (!iconPath) {
            if (showPlaceholder) {
                setImageUrl(imageService.getPlaceholderUrl());
            }
            setLoading(false);
            return;
        }

        setLoading(true);
        setError(false);

        // Determine size based on use case if not explicitly provided
        const imageSize = size || imageService.getSizeForUseCase(useCase);
        
        // Get optimized image URL
        const url = imageService.getImageUrl(iconPath, { format, size: imageSize });
        setImageUrl(url);

        // Preload the image to handle loading states properly
        const img = new Image();
        
        img.onload = () => {
            setLoading(false);
            setError(false);
            if (onLoad) onLoad();
        };
        
        img.onerror = () => {
            setLoading(false);
            setError(true);
            if (showPlaceholder) {
                setImageUrl(imageService.getPlaceholderUrl());
            }
            if (onError) onError();
        };
        
        img.src = url;
        
    }, [iconPath, size, format, useCase, showPlaceholder, onLoad, onError]);

    const handleImageLoad = () => {
        setLoading(false);
        if (onLoad) onLoad();
    };

    const handleImageError = () => {
        setError(true);
        setLoading(false);
        if (showPlaceholder) {
            setImageUrl(imageService.getPlaceholderUrl());
        }
        if (onError) onError();
    };

    if (!imageUrl && !showPlaceholder) {
        return null;
    }

    return (
        <div className={`destiny-image-container ${className} ${loading ? 'loading' : ''} ${error ? 'error' : ''}`}>
            {loading && (
                <div className="destiny-image-placeholder">
                    <div className="loading-shimmer"></div>
                </div>
            )}
            
            {imageUrl && (
                <img
                    src={imageUrl}
                    alt={alt}
                    className="destiny-image"
                    onLoad={handleImageLoad}
                    onError={handleImageError}
                    loading="lazy"
                    {...props}
                />
            )}
            
            {error && !showPlaceholder && (
                <div className="destiny-image-error">
                    <span>⚠️</span>
                </div>
            )}
        </div>
    );
};

export default DestinyImage;