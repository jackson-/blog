var showRecent = function(){
  document.getElementById('recentContainer').style.display = "inline-block";
  document.getElementById('popularContainer').style.display = "none";
  $('#2').removeClass("activeCategory");
  $('#1').addClass("activeCategory");
};

var showPopular = function(){
  document.getElementById('popularContainer').style.display = "inline-block";
  document.getElementById('recentContainer').style.display = "none";
  $('#1').removeClass("activeCategory");
  $('#2').addClass("activeCategory");
};
