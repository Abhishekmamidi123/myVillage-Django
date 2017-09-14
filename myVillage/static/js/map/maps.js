function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 16,
    center: {lat: 17.766, lng: 80.805}
  });
  var lat1=0;
  var lon1=0;
  var house;

  // var houselist = JSON.parse({{houselist|safe}});
  var houselist = JSON.parse('{{ houselist|safe }}');
  console.log(houselist);
  for (house in houselist){
      var l = house.lat ;
      var contentString = '<div id="content">'+
          '<div id="siteNotice">'+
          '</div>'+
          '<h1 id="firstHeading" class="firstHeading">Heading</h1>'+
          '<div id="bodyContent">'+
          '<p>Latitude:15.912 </p>' +
          '<p>Longitude:80.976</p>' +
      '<p>Depth:230m</p>' +
      '<p>Avg. Water yield:20 </p>' +
          '</div>'+
          '</div>';

      var uluru = {lat: 17.766, lng: 80.805};
      var infowindow = new google.maps.InfoWindow({
        content: contentString
      });

      var marker = new google.maps.Marker({
        position: uluru,
        map: map,
         icon:"/static/images/h.png",

        title: 'Uluru (Ayers Rock)'
      });
      marker.addListener('click', function() {
        infowindow.open(map, marker);
      });
      lat1 = lat1+0.001;
      lon1 = lon1+0.001;
  }
}
