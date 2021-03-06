cordova.define('cordova/plugin_list', function(require, exports, module) {
  module.exports = [
    {
      "id": "com.unarin.cordova.beacon.underscorejs",
      "file": "plugins/com.unarin.cordova.beacon/www/lib/underscore-min-1.6.js",
      "pluginId": "com.unarin.cordova.beacon",
      "runs": true
    },
    {
      "id": "com.unarin.cordova.beacon.Q",
      "file": "plugins/com.unarin.cordova.beacon/www/lib/q.min.js",
      "pluginId": "com.unarin.cordova.beacon",
      "runs": true
    },
    {
      "id": "com.unarin.cordova.beacon.LocationManager",
      "file": "plugins/com.unarin.cordova.beacon/www/LocationManager.js",
      "pluginId": "com.unarin.cordova.beacon",
      "merges": [
        "cordova.plugins"
      ]
    },
    {
      "id": "com.unarin.cordova.beacon.Delegate",
      "file": "plugins/com.unarin.cordova.beacon/www/Delegate.js",
      "pluginId": "com.unarin.cordova.beacon",
      "runs": true
    },
    {
      "id": "com.unarin.cordova.beacon.Region",
      "file": "plugins/com.unarin.cordova.beacon/www/model/Region.js",
      "pluginId": "com.unarin.cordova.beacon",
      "runs": true
    },
    {
      "id": "com.unarin.cordova.beacon.Regions",
      "file": "plugins/com.unarin.cordova.beacon/www/Regions.js",
      "pluginId": "com.unarin.cordova.beacon",
      "runs": true
    },
    {
      "id": "com.unarin.cordova.beacon.CircularRegion",
      "file": "plugins/com.unarin.cordova.beacon/www/model/CircularRegion.js",
      "pluginId": "com.unarin.cordova.beacon",
      "runs": true
    },
    {
      "id": "com.unarin.cordova.beacon.BeaconRegion",
      "file": "plugins/com.unarin.cordova.beacon/www/model/BeaconRegion.js",
      "pluginId": "com.unarin.cordova.beacon",
      "runs": true
    },
    {
      "id": "cordova-plugin-device.device",
      "file": "plugins/cordova-plugin-device/www/device.js",
      "pluginId": "cordova-plugin-device",
      "clobbers": [
        "device"
      ]
    },
    {
      "id": "cordova-plugin-device-orientation.CompassError",
      "file": "plugins/cordova-plugin-device-orientation/www/CompassError.js",
      "pluginId": "cordova-plugin-device-orientation",
      "clobbers": [
        "CompassError"
      ]
    },
    {
      "id": "cordova-plugin-device-orientation.CompassHeading",
      "file": "plugins/cordova-plugin-device-orientation/www/CompassHeading.js",
      "pluginId": "cordova-plugin-device-orientation",
      "clobbers": [
        "CompassHeading"
      ]
    },
    {
      "id": "cordova-plugin-device-orientation.compass",
      "file": "plugins/cordova-plugin-device-orientation/www/compass.js",
      "pluginId": "cordova-plugin-device-orientation",
      "clobbers": [
        "navigator.compass"
      ]
    },
    {
      "id": "cordova-plugin-inappbrowser.inappbrowser",
      "file": "plugins/cordova-plugin-inappbrowser/www/inappbrowser.js",
      "pluginId": "cordova-plugin-inappbrowser",
      "clobbers": [
        "cordova.InAppBrowser.open",
        "window.open"
      ]
    },
    {
      "id": "cordova-plugin-splashscreen.SplashScreen",
      "file": "plugins/cordova-plugin-splashscreen/www/splashscreen.js",
      "pluginId": "cordova-plugin-splashscreen",
      "clobbers": [
        "navigator.splashscreen"
      ]
    },
    {
      "id": "cordova-plugin-statusbar.statusbar",
      "file": "plugins/cordova-plugin-statusbar/www/statusbar.js",
      "pluginId": "cordova-plugin-statusbar",
      "clobbers": [
        "window.StatusBar"
      ]
    },
    {
      "id": "ionic-plugin-keyboard.keyboard",
      "file": "plugins/ionic-plugin-keyboard/www/ios/keyboard.js",
      "pluginId": "ionic-plugin-keyboard",
      "clobbers": [
        "cordova.plugins.Keyboard"
      ],
      "runs": true
    }
  ];
  module.exports.metadata = {
    "com.unarin.cordova.beacon": "3.3.0",
    "cordova-plugin-device": "1.1.5",
    "cordova-plugin-device-orientation": "1.0.6",
    "cordova-plugin-inappbrowser": "1.3.1-dev",
    "cordova-plugin-splashscreen": "4.0.2",
    "cordova-plugin-statusbar": "2.2.2",
    "cordova-plugin-whitelist": "1.3.2",
    "ionic-plugin-keyboard": "2.2.1"
  };
});