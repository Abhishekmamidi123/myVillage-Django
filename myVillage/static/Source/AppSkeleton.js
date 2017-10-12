function randomValue() {
  var value = Math.round(Math.random() * 100);
  chart.arrows[0].setValue(value);
  chart.axes[0].setTopText(value + " %");
  // adjust darker band to new value
  chart.axes[0].bands[1].setEndValue(value);
}

(function () {
    "use strict";




   Cesium.BingMapsApi.defaultKey = 'AihaXS6TtE_olKOVdtkMenAMq1L5nDlnU69mRtNisz1vZavr1HhdqGRNkB2Bcqvs'; // For use with this application only

    //////////////////////////////////////////////////////////////////////////
    // Creating the Viewer
    //////////////////////////////////////////////////////////////////////////

    //var viewer = new Cesium.Viewer('cesiumContainer');

    var viewer = new Cesium.Viewer('cesiumContainer', {

        // imageryProvider: new Cesium.MapboxImageryProvider({
        //     mapId: 'mapbox.streets',
        //     accessToken: 'pk.eyJ1IjoicmFqYWxha3NobWktdjE1IiwiYSI6ImNqOGh3NXlodDBzajMycW82NTQxNWNwM2QifQ.kdZbec2sVTm4aFplSeaizw'
        // }),
        scene3DOnly: true,
        selectionIndicator: true,
        baseLayerPicker: true
    });
    //////////////////////////////////////////////////////////////////////////
    // Loading Imagery
    //////////////////////////////////////////////////////////////////////////

    //Add Bing imagery
//     viewer.imageryLayers.addImageryProvider(new Cesium.BingMapsImageryProvider({
//         url : 'https://dev.virtualearth.net',
//         mapStyle: Cesium.BingMapsStyle.AERIAL // Can also use Cesium.BingMapsStyle.ROAD
//     }));

//     // //////////////////////////////////////////////////////////////////////////
//     // // Loading Terrain
//     // //////////////////////////////////////////////////////////////////////////

//     // Load STK World Terrain
//     viewer.terrainProvider = new Cesium.CesiumTerrainProvider({
//         url : 'https://assets.agi.com/stk-terrain/world',
//         requestWaterMask : true, // required for water effects
//         requestVertexNormals : false // required for terrain lighting
//     });
//     // Enable depth testing so things behind the terrain disappear.
//     // viewer.scene.globe.depthTestAgainstTerrain = true;

    //////////////////////////////////////////////////////////////////////////
    // Configuring the Scene
    //////////////////////////////////////////////////////////////////////////

    // Enable lighting based on sun/moon positions
    viewer.scene.globe.enableLighting = true;
    var place_coordinates = [13.086119,   80.261317,
13.085408,   80.267519,
13.086871,   80.276295,
13.080768,   80.280436,
13.078678,   80.268956,
13.080706,   80.261124,
13.081756,   80.271606,
13.080344,   80.283];
   var place_moisture_content = [86,
81,
82,
84,
86,
86,
82,
85];

    // Create an initial camera view
    var initialPosition = new Cesium.Cartesian3.fromDegrees(place_coordinates[1], place_coordinates[0], 2631.082799425431);
    var initialOrientation = new Cesium.HeadingPitchRoll.fromDegrees(7.1077496389876024807, -31.987223091598949054, 0.025883251314954971306);
    var homeCameraView = {
        destination : initialPosition,
        orientation : {
            heading : initialOrientation.heading,
            pitch : initialOrientation.pitch,
            roll : initialOrientation.roll
        }
    };
    // Set the initial view
    viewer.scene.camera.setView(homeCameraView);

    // Add some camera flight animation options
    homeCameraView.duration = 2.0;
    homeCameraView.maximumHeight = 2000;
    homeCameraView.pitchAdjustHeight = 2000;
    homeCameraView.endTransform = Cesium.Matrix4.IDENTITY;
    // Override the default home button
    viewer.homeButton.viewModel.command.beforeExecute.addEventListener(function (e) {
        e.cancel = true;
        viewer.scene.camera.flyTo(homeCameraView);
    });

    // Set up clock and timeline.
    viewer.clock.shouldAnimate = true; // default
    viewer.clock.startTime = Cesium.JulianDate.fromIso8601("2017-07-11T16:00:00Z");
    viewer.clock.stopTime = Cesium.JulianDate.fromIso8601("2017-07-11T16:20:00Z");
    viewer.clock.currentTime = Cesium.JulianDate.fromIso8601("2017-07-11T16:00:00Z");
    viewer.clock.multiplier = 2; // sets a speedup
    viewer.clock.clockStep = Cesium.ClockStep.SYSTEM_CLOCK_MULTIPLIER; // tick computation mode
    viewer.clock.clockRange = Cesium.ClockRange.LOOP_STOP; // loop at the end
    viewer.timeline.zoomTo(viewer.clock.startTime, viewer.clock.stopTime); // set visible range

    //////////////////////////////////////////////////////////////////////////
    // Loading and Styling Entity Data
    //////////////////////////////////////////////////////////////////////////

    // var kmlOptions = {
    //     camera : viewer.scene.camera,
    //     canvas : viewer.scene.canvas,
    //     clampToGround : true
    // };
var pinBuilder = new Cesium.PinBuilder();

var boxes = new Array(place_moisture_content.length);
var billboards = new Array(place_moisture_content.length);

var threshold = 83;
var blue_val; var green_val; var red_val;

 for (var j = 0; j < place_moisture_content.length; ++j)
 {
    var  i = j;
    if(place_moisture_content[i] < threshold){
        red_val = 1; blue_val = green_val = 0;
    }
    else
    {
        red_val = blue_val = 0; green_val = 1;
    }
boxes[i]= viewer.entities.add({
    name : 'box '+i,
    position: Cesium.Cartesian3.fromDegrees(place_coordinates[2*i+1], place_coordinates[2*i], 0),
    box : {
        dimensions : new Cesium.Cartesian3(100.0, 100.0, place_moisture_content[i]*place_moisture_content[i]),
        material : Cesium.Color.fromRandom({
            red: red_val,
            green: green_val,
            blue: blue_val,
            alpha: 0.8
        }),
    heightReference : Cesium.HeightReference.CLAMP_TO_GROUND,
        }

});

billboards[i] = viewer.entities.add({
    name: "bill"+i,
    position: Cesium.Cartesian3.fromDegrees(place_coordinates[2*i+1], place_coordinates[2*i], 0),
    billboard :{
        image : pinBuilder.fromColor(Cesium.Color.ROYALBLUE, 40).toDataURL(),
        verticalOrigin : Cesium.VerticalOrigin.BOTTOM

    }
});

boxes[i].description = '<div id="chartdiv"></div>';
    console.log(place_moisture_content[i]);
}

    var previousPickedEntity;
    var handler = viewer.screenSpaceEventHandler;
    handler.setInputAction(function (movement) {
        var pickedPrimitive = viewer.scene.pick(movement.endPosition);
        var pickedEntity = Cesium.defined(pickedPrimitive) ? pickedPrimitive.id : undefined;
        // console.log(pickedEntity);
        // // Unhighlight the previously picked entity
        if (Cesium.defined(previousPickedEntity)) {
            previousPickedEntity.billboard.scale = 1.0;
            previousPickedEntity.billboard.color = Cesium.Color.WHITE;
        }
        // Highlight the currently picked entity
        if (Cesium.defined(pickedEntity) && Cesium.defined(pickedEntity.billboard)) {

            pickedEntity.billboard.scale = 2.0;
            pickedEntity.billboard.color = Cesium.Color.ORANGERED;
            var chart = AmCharts.makeChart("infoWindow", {
  "theme": "light",
  "type": "gauge",
  "axes": [{
    "topTextFontSize": 20,
    "topTextYOffset": 70,
    "axisColor": "#31d6ea",
    "axisThickness": 1,
    "endValue": 100,
    "gridInside": true,
    "inside": true,
    "radius": "50%",
    "valueInterval": 10,
    "tickColor": "#67b7dc",
    "startAngle": -90,
    "endAngle": 90,
    "unit": "%",
    "bandOutlineAlpha": 0,
    "bands": [{
      "color": "#0080ff",
      "endValue": 100,
      "innerRadius": "105%",
      "radius": "170%",
      "gradientRatio": [0.5, 0, -0.5],
      "startValue": 0
    }, {
      "color": "#3cd3a3",
      "endValue": 0,
      "innerRadius": "105%",
      "radius": "170%",
      "gradientRatio": [0.5, 0, -0.5],
      "startValue": 0
    }]
  }],
  "arrows": [{
    "alpha": 1,
    "innerRadius": "35%",
    "nailRadius": 0,
    "radius": "170%"
  }]
});

setInterval(randomValue, 2000);

// set random value
function randomValue() {
  var value = Math.round(Math.random() * 100);
  chart.arrows[0].setValue(value);
  chart.axes[0].setTopText(value + " %");
  // adjust darker band to new value
  chart.axes[0].bands[1].setEndValue(value);
}
            previousPickedEntity = pickedEntity;

        }
    }, Cesium.ScreenSpaceEventType.MOUSE_MOVE);


var startLongitude = place_coordinates[1];
var endLongitude = place_coordinates[3];
var startLatitude = place_coordinates[0];
var endLatitude = place_coordinates[2];

viewer.entities.add({
    polyline : {
        positions : Cesium.Cartesian3.fromDegreesArray([startLongitude, startLatitude,
                                                               endLongitude, endLatitude]),
        width : 10,
        material : new Cesium.PolylineArrowMaterialProperty(Cesium.Color.YELLOW)
    }
});


var geodesic = new Cesium.EllipsoidGeodesic(Cesium.Cartographic.fromDegrees(startLongitude, startLatitude), Cesium.Cartographic.fromDegrees(endLongitude, endLatitude));
var value = 0;
var cartographicPosition = new Cesium.Cartographic();
var point  = viewer.entities.add({
    position: new Cesium.CallbackProperty(function(){
        var cartographic = geodesic.interpolateUsingFraction(value, cartographicPosition);
        var position = Cesium.Cartesian3.fromRadians(cartographic.longitude, cartographic.latitude);
        value = value > 1 ? 0 : value + 0.005;
        return position;
    }, false),
    point: {
        color : Cesium.Color.YELLOW,
        pixelSize : 20
    }
});

}());
