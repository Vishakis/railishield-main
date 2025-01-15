window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: function(config) {
            config.mapboxOptions = config.mapboxOptions || {};
            config.mapboxOptions.dragPan = true; // Enable dragging for panning
            config.mapboxOptions.dragRotate = false; // Disable right-click rotation
            return config;
        }

    }
});