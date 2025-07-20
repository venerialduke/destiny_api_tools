"""
Image proxy and caching API endpoints.
"""

from flask import Blueprint, request, Response, jsonify
from ...services.image_service import get_image_service
import urllib.parse

images_bp = Blueprint('images', __name__)


@images_bp.route('/proxy/<path:icon_path>', methods=['GET'])
def proxy_image(icon_path):
    """
    Proxy and cache Bungie images with optional processing.
    
    Query parameters:
    - format: webp, jpg, png (default: original)
    - size: small, medium, large, or WxH (e.g., 96x96)
    """
    try:
        # Ensure icon_path starts with /
        if not icon_path.startswith('/'):
            icon_path = '/' + icon_path
        
        # Get query parameters
        format_param = request.args.get('format', 'original').lower()
        size_param = request.args.get('size')
        
        # Validate format parameter
        valid_formats = ['original', 'webp', 'jpg', 'jpeg', 'png']
        if format_param not in valid_formats:
            format_param = 'original'
        
        image_service = get_image_service()
        
        # Try to get from cache first
        cached_result = image_service.get_cached_image(icon_path, format_param, size_param)
        
        if cached_result:
            image_data, content_type, cached_time = cached_result
            
            # Create response with cache headers
            response = Response(image_data, content_type=content_type)
            response.headers['Cache-Control'] = 'public, max-age=86400'  # 24 hours
            response.headers['X-Cache-Status'] = 'HIT'
            response.headers['X-Cache-Time'] = cached_time.isoformat()
            
            return response
        
        # Not in cache, download and cache
        download_result = image_service.download_and_cache_image(icon_path, format_param, size_param)
        
        if download_result:
            image_data, content_type = download_result
            
            # Create response
            response = Response(image_data, content_type=content_type)
            response.headers['Cache-Control'] = 'public, max-age=86400'  # 24 hours
            response.headers['X-Cache-Status'] = 'MISS'
            
            return response
        else:
            # Download failed, return 404
            return jsonify({'error': 'Image not found or download failed'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@images_bp.route('/url/<path:icon_path>', methods=['GET'])
def get_image_url(icon_path):
    """
    Get optimized image URL for client-side usage.
    
    Query parameters:
    - format: webp, jpg, png (default: webp)
    - size: small, medium, large, or WxH
    """
    try:
        # Ensure icon_path starts with /
        if not icon_path.startswith('/'):
            icon_path = '/' + icon_path
        
        format_param = request.args.get('format', 'webp').lower()
        size_param = request.args.get('size')
        
        image_service = get_image_service()
        proxy_url = image_service.get_image_url(icon_path, format_param, size_param)
        
        # Return full URL with host
        full_url = request.host_url.rstrip('/') + proxy_url
        
        return jsonify({
            'icon_path': icon_path,
            'proxy_url': proxy_url,
            'full_url': full_url,
            'format': format_param,
            'size': size_param,
            'original_url': f"https://www.bungie.net{icon_path}"
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@images_bp.route('/batch-urls', methods=['POST'])
def get_batch_image_urls():
    """
    Get optimized URLs for multiple images.
    
    Request body:
    {
        "icon_paths": ["/path1", "/path2", ...],
        "format": "webp",
        "size": "medium"
    }
    """
    try:
        data = request.get_json()
        if not data or 'icon_paths' not in data:
            return jsonify({'error': 'Missing icon_paths array'}), 400
        
        icon_paths = data['icon_paths']
        format_param = data.get('format', 'webp').lower()
        size_param = data.get('size')
        
        if len(icon_paths) > 100:
            return jsonify({'error': 'Maximum 100 images per request'}), 400
        
        image_service = get_image_service()
        results = {}
        
        for icon_path in icon_paths:
            if not icon_path.startswith('/'):
                icon_path = '/' + icon_path
            
            proxy_url = image_service.get_image_url(icon_path, format_param, size_param)
            full_url = request.host_url.rstrip('/') + proxy_url
            
            results[icon_path] = {
                'proxy_url': proxy_url,
                'full_url': full_url,
                'original_url': f"https://www.bungie.net{icon_path}"
            }
        
        return jsonify({
            'images': results,
            'format': format_param,
            'size': size_param,
            'count': len(results)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@images_bp.route('/cache/stats', methods=['GET'])
def get_cache_stats():
    """Get image cache statistics."""
    try:
        image_service = get_image_service()
        stats = image_service.get_cache_stats()
        
        return jsonify({
            'cache_statistics': stats,
            'status': 'healthy' if stats['cache_usage_percent'] < 90 else 'warning',
            'recommendations': _get_cache_recommendations(stats)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@images_bp.route('/cache/clear', methods=['POST'])
def clear_cache():
    """Clear the image cache."""
    try:
        image_service = get_image_service()
        image_service.clear_cache()
        
        return jsonify({
            'success': True,
            'message': 'Image cache cleared successfully'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@images_bp.route('/formats', methods=['GET'])
def get_supported_formats():
    """Get information about supported image formats and sizes."""
    return jsonify({
        'formats': {
            'original': 'Keep original format (fastest)',
            'webp': 'WebP format (best compression, modern browsers)',
            'jpg': 'JPEG format (universal compatibility)',
            'png': 'PNG format (lossless, supports transparency)'
        },
        'sizes': {
            'original': 'Keep original size',
            'small': '64x64 pixels',
            'medium': '128x128 pixels', 
            'large': '256x256 pixels',
            'custom': 'Specify as WIDTHxHEIGHT (e.g., 96x96)'
        },
        'recommendations': {
            'thumbnails': 'format=webp&size=small',
            'cards': 'format=webp&size=medium',
            'detailed_view': 'format=webp&size=large',
            'maximum_compatibility': 'format=jpg&size=medium'
        },
        'performance_tips': [
            'Use WebP format for 25-35% smaller file sizes',
            'Use appropriate sizes to reduce bandwidth',
            'Images are cached for 7 days locally',
            'Cache has 24-hour browser cache headers'
        ]
    })


def _get_cache_recommendations(stats):
    """Get cache optimization recommendations."""
    recommendations = []
    
    if stats['cache_usage_percent'] > 90:
        recommendations.append('Cache is nearly full - consider clearing old entries')
    
    if stats['hit_rate_percent'] < 50:
        recommendations.append('Low cache hit rate - consider increasing cache size')
    
    if stats['errors'] > stats['downloads'] * 0.1:
        recommendations.append('High error rate - check network connectivity')
    
    if stats['cache_size_mb'] < 100 and stats['total_requests'] > 1000:
        recommendations.append('Consider increasing cache size for better performance')
    
    if not recommendations:
        recommendations.append('Cache is performing well')
    
    return recommendations